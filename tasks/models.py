from django.db import models

from projects.models import Project
from .choices import STATUS_CHOICES

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = 'tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_description(self):
        return self.description

    def set_descriptoin(self, description):
        self.description = description
    
    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
    
    def get_project(self):
        return self.project
    
    def set_project(self, project):
        self.project = project
    
    @classmethod
    def get_completed_tasks(cls):
        return cls.objects.filter(status='completed')
    
    @classmethod
    def get_in_progress_tasks(cls):
        return cls.objects.filter(status='in_progress')
    
    @classmethod
    def get_not_started_tasks(cls):
        return cls.objects.filter(status='not_started')
