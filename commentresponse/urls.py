from django.urls import path
from .views import SSCommentResponseView

app_name = 'commentresponse'

urlpatterns = [
    path('ss/', SSCommentResponseView.as_view(), name='ss-crboard'),
]