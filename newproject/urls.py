"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from sample import views
from sample import views
from sale.views import test, register, search, delete, detail, update, message
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('home/', views.about, name='about1'),
                  path('contact/', views.contact, name='contact'),
                  path('gallery/', views.gallery, name='gallery'),
                  path('about/', test, name='about'),
                  path('register/', register, name='register'),
                  path('search/', search, name='search'),
                  path('delete/<int:id>', delete, name='delete'),
                  path('detail/<int:id>', detail, name='detail'),
                  path('update/<int:id>', update, name='update'),
                  path('messgae/', message, name='message'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
