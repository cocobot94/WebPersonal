
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Portfolio import views

urlpatterns = [
     path('portfolio',views.portfolio,name='portfolio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)