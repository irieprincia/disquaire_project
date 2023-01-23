from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking
from django.utils.datastructures import MultiValueDictKeyError
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from .forms import ContactForm, ParagraphErrorList
from django.db import transaction, IntegrityError



def index(request):
    albums=Album.objects.all().order_by('-created_at')[:3]

    template='store/index.html'

    return render(request, template, {"albums":albums})

    #return HttpResponse(template.render(context, request=request))

def listing(request):
    albums_list=Album.objects.all()
    paginator=Paginator(albums_list, 2)
    page=request.GET.get('page')
    try:
        albums=paginator.page(page)

    except PageNotAnInteger:
        albums=paginator.page(1)

    except EmptyPage:
        albums=paginator.page(paginator.num_pages)

    template='store/listing.html'
    context={
        "albums":albums,
        "paginate": True
    }

    return render(request, template, context)


def detail(request, album_id):

    album = get_object_or_404(Album, id=album_id)
    artists=[artist.name for artist in album.album_artist.all()]
    artists_name="".join(artists)
    context={
        'album': album,
        # "album_title":album.title,
        "artists_name":artists_name,
        # "album_id":album.id,
        # "thumbnail":album.picture,
    }

    if request.method== 'POST':
        form=ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            form.save()

            try: 
                with transaction.atomic():
                    contact=Contact.objects.filter(email=email)
                    if not contact.exists():
                        contact=Contact.objects.create(
                            email=email,
                            name=name
                        )
                    else: 
                        contact=contact.first()

                    if album.storage > 0:
                        booking=Booking.objects.create(
                            contact=contact,
                            album=album
                        )

                        album.storage = album.storage - 1
                        album.save()

                        if album.storage == 0:
                            album.available=False
                            album.save()
                                     
            except IntegrityError:
                form.errors['internal']= "Une erreur interne est apparue. Merci de recommencer votre requête."
                context['errors']=form.errors.items() 

    else:
        form=ContactForm()

    context['form'] = form
    
    
    template='store/detail.html'
    return render(request, template, context)



def search(request):
    query=request.GET.get('query')

    if not query:
       albums=Album.objects.all()

    else:
        albums=Album.objects.filter(title__icontains=query)
        
    if not albums.exists():
        albums=Album.objects.filter(album_artist__name__icontains=query)

    
    title="Résultats pour la requête %s"%query
    template='store/search.html'
    context={
        'albums':albums,
        'title':title
    }
    return render(request, template, context)


