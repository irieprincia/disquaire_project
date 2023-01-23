from django.test import TestCase
from django.urls import reverse
from .models import Album, Artist, Contact, Booking



#Index page
    #tesT that index page returns a 200
class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response=self.client.get(reverse('store:index'))
        self.assertEqual(response.status_code, 200)


#DETAIL PAGE
class DetailPageTestCase(TestCase):

    #ran before each test
    def setUp(self):
        Contact.objects.create(name="Freddie", email="fred@queen.forever")
        impossible = Album.objects.create(title="Transmission Impossible")
        journey = Artist.objects.create(name="Journey")
        impossible.album_artist.add(journey)
        self.album = Album.objects.get(title='Transmission Impossible')
        self.contact = Contact.objects.get(name = 'Freddie')

    #test that detail page returns a 200 IF THE ITEM exists
    def test_detail_page_returns_200(self):
        impossible=Album.objects.create(title="Transmission Impossible")
        album_id=Album.objects.get(title='Transmission Impossible').id 
        response=self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    #test that detail page returns a 404 if the item does not exists
    def test_detail_page_returns_404(self):
        impossible=Album.objects.create(title="Transmission Impossible")
        album_id=Album.objects.get(title='Transmission Impossible').id + 1
        response=self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)

    class BookingPageTestCase(TestCase):

        #test that a new booking is made
        def test_new_booking_is_registered(self):
            old_bookings= Booking.objects.count()
            album_id = self.album.id
            name = self.contact.name
            email = self.contact.email 
            response = self.client.post(reverse('store:detail', args=(album_id,)), {
                'name': name,
                'email': email
            })
            new_bookings= Booking.objects.count()
            self.assertEqual(new_bookings, old_bookings +1)


#Booking page
    #test that a new booking is made
    #test that a booking belongs to a contact
    #test that a booking belongs to a album
    #test that an album is not available after a booking is made


