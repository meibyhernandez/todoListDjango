from django.urls import path 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
     path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
     path('create-task/', TaskCreate.as_view(), name='create-task'),
     path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
     path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
     
]