from django.db import models

# Create your models here.

class Project(models.Model) : 
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date =  models.DateField()
    end_date = models.DateField()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
    
    def get_start_date(self):
        return self.start_date
    
    def set_start_date(self, start_date):
        self.start_date = start_date
    
    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date
    
    def get_tasks(self):
        return self.tasks.all()


    