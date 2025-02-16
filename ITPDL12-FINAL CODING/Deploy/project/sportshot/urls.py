from django.urls import path
from . import views

urlpatterns = [
    path('', views.sport_model, name='sport_model'),
    path('model_database/', views.sport_database, name='sport_database')
]
