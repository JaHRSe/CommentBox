from django.urls import path
from .views import  index, Save, SSDashboardView, HRADashboardView, SSCommentResponse

app_name = 'cbAdmin'

urlpatterns = [

    path('', index, name='dashboard'),
    path('ss/', SSDashboardView.as_view(), name='ss-dashboard'),
    path('hra/', HRADashboardView.as_view(), name='hra-dashboard'),
    path('ss/commentresponse/', SSCommentResponse.as_view(), name='ss-commentresponse'),
   # path('save/', Save.as_view(), name='save'),
]