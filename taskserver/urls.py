from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.task_list, name='task_list'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-update/<int:id>/', views.task_update, name='task_update'),
    path('task-delete/<int:id>/', views.task_delete, name='task_delete'),
    path('task-detail/<int:id>/', views.task_detail, name='task_detail'),
    path('complete-tasks/', views.complete_tasks, name='complete_tasks'),
    path('incomplete-task/<int:id>/', views.incomplete_task, name='incompleteTasks'),
    # path('task-create/', views.handlepriority, name='priority'),
]