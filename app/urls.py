from django.urls import path
from . import views
from app.views import UserProfileView, SendPasswordResetEmailView,UserPasswordResetView, UserLoginView, UserAPI, ProjectAPI, UserChangePasswordView, ServiceAPI, ExperienceAPI, EducationAPI, experience_get, education_get, project_get, services_get, users_get
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('project/', ProjectAPI.as_view(), name='project'),
    path('project/<int:pk>/', ProjectAPI.as_view(), name='project'),
    path('user/', UserAPI.as_view(), name='user'),
    path('user/<int:pk>/', UserAPI.as_view(), name='user'),
    path('service/', ServiceAPI.as_view(), name='service'),
    path('service/<int:pk>/', ServiceAPI.as_view(), name='service'),
    path('experience/', ExperienceAPI.as_view(), name='experience'),
    path('experience/<int:pk>/', ExperienceAPI.as_view(), name='experience'),
    path('education/', EducationAPI.as_view(), name='education'),
    path('education/<int:pk>/', EducationAPI.as_view(), name='education'),
    path('changepassword/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-email/',
         SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),



    # ----------------------functional components-----------------
    path('projects/', views.project_get, name='project_list'),
    path('projects/<int:pk>/', views.project_get, name='project'),
    path('services/', views.services_get, name='services_list'),
    path('services/<int:pk>/', views.services_get, name='service'),
    path('users/<int:pk>/', views.users_get, name='user'),
    path('users/', views.users_get, name='user_list'),
    path('experiences/', views.experience_get, name='experience_list'),
    path('experiences/<int:pk>/', views.experience_get, name='experience_list'),
    path('educations/', views.education_get, name='education_list'),
    path('educations/<int:pk>/', views.education_get, name='education_list')



]
