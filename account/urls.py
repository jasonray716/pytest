from django.conf.urls import include, url
from . import views

accounts_urls = [
	url(r'^$', views.index),
    url(r'^new', views.newAccount),
    url(r'^edit/(?P<id_account>.*)', views.editAccount),
    url(r'^delete/(?P<id_account>.*)', views.deleteAccount),
]


