from django.urls import path
from . import views

urlpatterns = [
    path('user/add/', views.user_form, name='user_form'),
    path('form/', views.many_fields_form, name='many_fields_form'),
    path('form2/', views.many_fields_form_widget, name='many_fields_form_widget'),
    path('user/', views.add_user, name='add_user'),
    path('image/', views.upload_image, name='upload_image'),

]
