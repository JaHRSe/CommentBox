from django.urls import path
from .views import Comment

app_name = 'comment'

urlpatterns = [

    path('', Comment.as_view(), name='comment'),
]