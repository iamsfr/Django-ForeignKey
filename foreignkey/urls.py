
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.data_form,name='data_form'),
    path('data/',views.data_read,name='data_read'),
]
