from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('submit_form_data/', views.submit_form_data, name='submit_form_data'),
    path('submit_field_data/', views.submit_field_data, name='submit_field_data'),
]
