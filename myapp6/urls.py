from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.total_in_view, name='view'),
    path('db/', views.total_in_db, name='db'),
    path('template/', views.total_in_template, name='template'),
]
