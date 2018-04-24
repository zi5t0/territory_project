from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.show_login),
    path(r'login/', views.handle_login),
    path(r'logout/', views.handle_logout),
    path(r'inicio/', views.show_index),
    path(r'restringido/', views.redirect_forbidden),
]