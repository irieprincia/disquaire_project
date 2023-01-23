from django.contrib import admin
from store.models import(Album, Booking, Contact, Artist)
#from django.contrib.contenttypes.models import ContentType
#from django.utils.safestring import mark_safe

#class AdminURLMixin(object):
 #   content_type=ContentType.object.get_for_model(obj.__class__)
 #   def get_admin_url(self, obj):
 #       return reverse("admin:store_%s_change" % (
  #          content_type.model),
   #         args=(obj.id,))


class AlbumAdmin(admin.ModelAdmin):
    list_display=('title', 'picture', 'storage')
    list_filter=('created_at', 'title')
    ordering=('title', 'reference')
    search_fields=('available', 'reference')



class BookingInline(admin.TabularInline):
    verbose_name="Réservation"
    verbose_name_plural="Réservations"
    model=Booking
    fieldsets=[
        (None, {'fields': ['album', 'created_at', 'Contacted']})

    ]
    extra=0
    readonly_fields=[ 'album', 'created_at']

   #def album_link(self, booking):
     #   url = self.get_admin_url(booking.album)
      #  return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    #def has_add_permission(self, request):
        #return False

class ContactAdmin(admin.ModelAdmin):
    inlines=[BookingInline,]

    
class AlbumArtistInline(admin.TabularInline):
    verbose_name="Disque"
    verbose_name_plural="Disques"
    model=Album.album_artist.through
    extra=1

class ArtistAdmin(admin.ModelAdmin):
    inlines=[AlbumArtistInline,]

class BookingAdmin(admin.ModelAdmin):
    list_filter=['created_at', 'Contacted',]
    fieldsets=[
        (None, {'fields': ['album', 'contact', 'created_at', 'Contacted']})
    ]
    readonly_fields=['album', 'contact', 'created_at', 'Contacted']

    #def contact_link(self, booking):
     #   url = self.get_admin_url(booking.contact)
     #   return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))
        
    #def album_link(self, booking):
      #  url=self.get_admin_url(obj.album)
       # return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    

admin.site.register(Album, AlbumAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Artist, ArtistAdmin)



