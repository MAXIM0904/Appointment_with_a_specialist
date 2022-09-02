from django.urls import path
from . import views


urlpatterns = [
    path('all_record/', views.AllRecord.as_view(), name='all_record'),
    path('create_record/', views.CreateRecord.as_view(), name='create_record'),
    path('delete/', views.DeleteRecord.as_view(), name='delete'),
]