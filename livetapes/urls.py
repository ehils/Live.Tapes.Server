"""app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from livetapes_api.views import register_user, login_user
from livetapes_api.views import ShowView, TrackView, ArtistView, LocationView, VenueView, PlaylistView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'shows', ShowView, 'show')
router.register(r'tracks', TrackView, 'track')
router.register(r'artists', ArtistView, 'artist')
router.register(r'locations', LocationView, 'location')
router.register(r'venues', VenueView, 'venue')
router.register(r'playlists', PlaylistView, 'playlist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls))
]
