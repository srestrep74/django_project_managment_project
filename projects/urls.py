from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index_project'),
    path('show_project/<int:project_id>/', views.show, name='show_project'),
    path('create_project/', views.create, name='create_project'),
    path('save_project/', views.save, name='save_project'),
    path('delete_project/<int:project_id>/', views.delete, name='delete_project'),
    path('destroy_project/<int:project_id>/', views.destroy, name='destroy_project'),
    path('edit_project/<int:project_id>/', views.edit, name='edit_project'),
    path('update_project/<int:project_id>/', views.update, name='update_project')
]