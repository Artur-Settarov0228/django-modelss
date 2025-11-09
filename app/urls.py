
from django.urls import path
from . views import create_task, task_list, counter_view, get_user, get_user_by_id, create_user

urlpatterns = [
    path('', create_task, name='create_task'),
    path('list/', task_list, name='task_list'),
    path('counter/', counter_view, name='counter_view'),
    path('users/<int:pk>', get_user_by_id, name='get_user'),
    path('users/<slug:slug>', get_user, name='get_user'),
    path('users/',  create_user, name='create_user'),
    
    
]