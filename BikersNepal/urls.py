"""BikersNepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from . import views, settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('index/', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('Yamaha/', views.yamaha, name='Yamaha'),
    path('Honda/', views.honda, name='Honda'),
    path('Suzuki/', views.suzuki, name='Suzuki'),
    path('Bajaj/', views.pulsar, name='Bajaj'),
    path('restricted/',views.home_restricted,name='user_details'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:pk>/', views.delete),
    path('deletey/<int:pk>/', views.deletey),
    path('deletes/<int:pk>/', views.deletes),
    path('deleteb/<int:pk>/', views.deleteb),
    path('update_form/<int:pk>/', views.update_form),
    path('update_form/update/<int:pk>/', views.update),
    path('register/', include('register.urls')),
    path('reserve/',include('reserve.urls')),
    path('signupform/', include('register.urls')),
    path('logout/', views.index, name="homepage"),
    path('logout_redirect/', views.logout_view, name="logout" ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





