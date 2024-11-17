from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_requests, name='manage_requests'),
    path('detail/<int:request_id>/', views.request_detail, name='request_detail'),
]
