from django.urls import path
from .views import DashboardView, Save

app_name = 'cbAdmin'

urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('save/', Save.as_view(), name='save'),
]