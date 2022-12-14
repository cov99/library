from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'readers/',
        views.ListReaders.as_view(),
        name="readers"
    ),
]
