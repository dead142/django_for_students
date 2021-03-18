from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # если пустая строка
    path('contact', views.contact, name='contact'),  # если пустая строка

]
