"""KSUvity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from KSUvity.authentication import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^$', authentication_views.dashboard, name='dashboard'),
    url(r'^home/', authentication_views.home, name='home'),
    url(r'^coord/', authentication_views.admin, name='admin'),
    url(r'^login/$', authentication_views.Login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'dashboard'}, name='logout'),
    url(r'^signup/$', authentication_views.signup, name='signup'),
    url(r'^(?P<pk>\d+)/register/$', authentication_views.registerAttendee, name='register'),
    url(r'^(?P<pk>\d+)/cancel/$', authentication_views.cancel, name='cancel'),
    url(r'^(?P<pk>\d+)/volunteer/$', authentication_views.registerVolunteer, name='volunteer'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # url(r'^reset/$', authentication_views.reset, name='reset'),
    url(r'^password/$', authentication_views.change_password, name='change_password'),
    url(r'^\d+/cancel/home/$', authentication_views.home, name='cancelHome'),
    url(r'^\d+/register/home/$', authentication_views.home, name='regHome'),
    url(r'^\d+/volunteer/home/$', authentication_views.home, name='volHome'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  
