from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
<<<<<<< HEAD
    path('comments/<int:pk>/', views.CommentDetail.as_view())
=======
    path('comments/<int:pk>', views.CommentDetail.as_view()),
    path('reply/', views.ReplyDetail.as_view())
>>>>>>> 5990a5313c6e897bf7b266e75dcc436522794dee
]