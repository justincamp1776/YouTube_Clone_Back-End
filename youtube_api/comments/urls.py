from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    path('comments/reply/', views.ReplyDetail.as_view())
]