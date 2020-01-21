from django.urls import path
from .views import Comment, HRAView, UploadView

app_name = 'comment'

urlpatterns = [

    path('', Comment.as_view(), name='comment'),
    path('hra/', HRAView.as_view(), name='hra_comment'),
    path('upload/', UploadView.as_view(), name='upload'),
]