from django.urls import path
from APICreditScore.views import apiCreditScore

app_name = 'api'
urlpatterns = [
    path('api/',apiCreditScore.as_view(),name="api")
]
