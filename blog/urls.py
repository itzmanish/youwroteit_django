from django.urls import path
from .views import google_login


urlpatterns = [
    path('', google_login, name='google_auth')
]
