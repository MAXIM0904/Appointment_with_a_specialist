from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('user_record/', views.user_record, name='user_record'),
    path('delete_pattern_record/', views.delete_pattern_record, name='delete_pattern_record'),
    path('delete_record/', views.delete_record, name='delete_record'),
    path('logging/', views.logging, name='logging'),
]