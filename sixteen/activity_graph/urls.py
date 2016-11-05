from django.conf.urls import url

from . import views

urlpatterns = [
    url (r'^$', views.index, name = 'index'),
    url (r'^account/$', views.account, name = 'account'),
    url (r'^(?P<extendedUser>[name]+)/$', views.feed, name = 'feed')
    url (r'^ /$', views.business, name = 'business')
]