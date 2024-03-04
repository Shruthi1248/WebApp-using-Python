from django.urls import path

from . import views
from .views import save_project

urlpatterns = [
    path('', views.home, name="home"),
    path('submit_form_data/', views.submit_form_data, name='submit_form_data'),
    path('submit_field_data/', views.submit_field_data, name='submit_field_data'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('save_project/', save_project, name='save_project'),
]

