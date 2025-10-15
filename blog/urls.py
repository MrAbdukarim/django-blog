from django.urls import path
from .views import BlogListView, BlogDetailView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', views.about_view, name='about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
