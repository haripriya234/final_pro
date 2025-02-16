from django.urls import path
from . import views

urlpatterns = [
    path('', views.usersignup, name='usersignup'),
    path('login/', views.loginpage, name='userlogin'),
    path('logout/', views.logoutusers, name='logoutusers'),
    path('Authorsignup/', views.authorsignup, name='Authorsignup'),
    path('Authorlogin/', views.authorlogin, name='Authorlogin'),
    path('Authlogout/', views.authorlogout, name='Authorlogout')
]
# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),

#     path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#     path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#     path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]