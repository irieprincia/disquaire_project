
from django.urls import path

from store.views import index, detail, search, listing


urlpatterns=[
      path('index/', index, name='index'),
      path('<int:album_id>/', detail, name='detail'),
      path('search/', search, name='search'),
      path('', listing, name='listing'),
]