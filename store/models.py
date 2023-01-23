from django.db import models
from django.conf import settings


class Artist(models.Model):
    name=models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="artiste"    


class Contact(models.Model):
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="client"



class Album(models.Model):
    reference=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=200)
    picture=models.ImageField(upload_to='disquaire_project')
    storage = models.IntegerField(default=0)

    album_artist=models.ManyToManyField(Artist, related_name='albums', blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="disque"



class Booking(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    Contacted=models.BooleanField(default=False)
    pre_commande=models.BooleanField(default=False)

    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    contact=models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name = "réservation"








