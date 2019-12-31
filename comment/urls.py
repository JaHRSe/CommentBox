from django.urls import path
from .views import Comment, UploadView

app_name = 'comment'

urlpatterns = [

    path('', Comment.as_view(), name='comment'),
    path('upload/', UploadView.as_view(), name='upload'),
]