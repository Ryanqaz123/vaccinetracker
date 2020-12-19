from django.urls import path
from . import views

app_name = 'Vaccine_App'
urlpatterns = [
    path('', views.LocationView.as_view(), name = 'location'),

]
