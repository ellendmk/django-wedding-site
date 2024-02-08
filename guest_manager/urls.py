from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic.base import RedirectView

from guest_manager import views


urlpatterns = [
    path('invite/<str:id_>',views.invite),
    path('rsvp_viewerdx5gsvsbunb8',views.rsvp_viewer),
    path('rsvp/<str:id_>',views.invite),
    path('details/<str:id_>',views.details),
    path('submit/<str:id_>',views.invite),
]