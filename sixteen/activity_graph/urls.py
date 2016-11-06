from django.conf.urls import url

from . import views

urlpatterns = [
    url (r'^$', views.index, name = 'index'),               # Home
    url (r'^account/$', views.account, name = 'account'),   # Login
    url (r'^feed/$', views.feed, name = 'feed'),            # Feed
    url (r'^(?P<business>[name]+)/$', views.business, name = 'business') # Detailed Info
]
