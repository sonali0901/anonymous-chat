from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'lnmiit_chat.views.home', name='home'),
     url(r'^chats/', include('chat.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
