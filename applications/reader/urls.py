from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'lendlease/add/',
        views.AddLendLease.as_view(),
        name="lendlease-add"
    ),
    path(
        'lendlease/multiple-add/',
        views.AddMultipleLendLease.as_view(),
        name="lendlease_add_multiple"
    ),
]
