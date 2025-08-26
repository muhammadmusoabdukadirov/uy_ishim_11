from django.contrib import admin
from django.urls import path
from .views import index, new_by_category, announcement_detail, add_app, update_app, delete_app

urlpatterns = [
    path('', index, name="index"), 
    path("app/add/", add_app, name="add_app"),
    path("app/update/<int:pk>/", update_app, name="update_announcement"),
    path("app/delete/<int:pk>/", delete_app, name="delete_app"),
    path('category/<int:category_id>/', new_by_category, name='news_by_category'),
    path('announcement/<int:pk>/', announcement_detail, name='announcement_detail'),
]
