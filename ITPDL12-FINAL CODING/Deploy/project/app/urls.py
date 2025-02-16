from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingpage'),
    path('home/', views.index, name='home'),
    path('problem_statement/', views.problem_statement , name='info'),
    path('player_information/', views.player_information, name='player_information'),
    path('team/', views.team, name='team'),
    path('sport_shot_model/', views.sport_shot_model , name='sport_shot_model'),
    path('player_dashboard/', views.player_dashboard, name='player_dashboard'),
    path('database/', views.player_database, name='database'),
    path('sport_shot_database/', views.sport_shot_database, name='sport_shot_database'),

    
    
    
]
