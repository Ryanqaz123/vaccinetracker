from django.urls import path
from . import views

app_name = 'Vaccine_App'
urlpatterns = [
    path('', views.LocationView.as_view(), name = 'location'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('update/', views.UpdateView.as_view(), name = 'update'),
    path('delete/', views.DeleteView.as_view(), name = 'delete'),
]
