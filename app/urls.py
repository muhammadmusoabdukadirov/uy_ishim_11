from django.contrib import admin
from django.urls import path
from .views import index, new_by_category, announcement_detail

urlpatterns = [
    path('', index, name="index"), 
    path('category/<int:category_id>/', new_by_category, name='news_by_category'),
    path('announcement/<int:pk>/', announcement_detail, name='announcement_detail'),
]
