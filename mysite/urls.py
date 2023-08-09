"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.static import serve
from django.conf.urls import include
from .views import admin, table_contents

# from django.conf.urls import path


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('layout', views.layout, name='layout.html'),
    path('contact', views.contact, name='contact.html'),
    path('', views.index, name='index.html'),
    path('table_contents/<str:table_name>/', table_contents, name='table_contents'),  # Correct URL pattern
    path('photos', views.photos, name='photos.html'),
    path('saveform', views.saveform, name='saveform'),
    path('mywork', views.mywork, name='mywork.html'),   
    path('admin', views.admin, name='login.html'),
    # path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

