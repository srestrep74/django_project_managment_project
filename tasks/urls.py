from django.urls import path
from . import views


urlpatterns = [
    path('project/<int:project_id>/', views.get_tasks, name='get_tasks'),
    path('create_task/<int:project_id>/', views.create, name='create_task'),
    path('save_task/<int:project_id>/', views.save, name='save_task'),
    path('edit_task/<int:task_id>/', views.edit, name='edit_task'),
    path('update_task/<int:task_id>/', views.update, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete, name='delete_task'),
    path('destroy_task/<int:task_id>/', views.destroy, name='destroy_task'),
    path('completed/', views.dones, name='completed_tasks'),
    path('in_progress/', views.in_progress, name='in_progress_tasks'),
    path('not_started/', views.undone, name='not_started_tasks')
]
