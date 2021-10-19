from django.urls import path
from . import views


urlpatterns = [
    path('comments/video/<str:id>', views.CommentList.as_view()), # Get all
    path('comments/<int:pk>', views.CommentDetail.as_view()), # Patch, Put, & Delete
    path('comments/reply/', views.ReplyDetail.as_view()), # ADD a reokt
    path('comments/reply/<int:commentId>', views.ReplyDetail.as_view()), # ADD a reokt
    path('comments/', views.CommentList.as_view()),
]