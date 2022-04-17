from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist/', AuthorList.as_view()),
    path('<int:pk>/', Post.as_view(), name='pk'),
    path('', PostList.as_view()),
]