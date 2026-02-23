from django.urls import path 
from .views import RegisterView, TaskListCreate, TaskDetail
from rest_framework.authtoken.views import obtain_auth_token # This line is where the built-in view was instantiated for us to use


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', obtain_auth_token, name='login'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]