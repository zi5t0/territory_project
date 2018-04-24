from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.show_list),
    path(r'list/', views.show_list),
    path(r'edit/', views.show_edit),
    path(r'handle_edit/', views.handle_edit),
    path(r'delete/', views.handle_delete),
]