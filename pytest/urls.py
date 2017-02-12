from django.conf.urls import patterns, include, url
from account.urls import accounts_urls
from django.contrib import admin

urlpatterns = [
	url(r'^', include(accounts_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
