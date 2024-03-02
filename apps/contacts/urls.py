from django.urls import path

from apps.contacts import views

urlpatterns = [
    path('contacts/', views.contacts, name='contacts')
]

