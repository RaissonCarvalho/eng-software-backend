from django.urls import path
from core import views

urlpatterns = [
    path('posts/', views.PostsList.as_view(), name=views.PostsList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
]