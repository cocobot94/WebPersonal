
from django.contrib import admin
from django.urls import path
from Core import views 
from Portfolio import views as porfolio_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.portada,name='portada'),
    path('about',views.about,name='about'),
    path('contact',views.conatct,name='contact'),
   
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)