from django.db import models
from videos.models import *

# Create your models here.

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name 

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=20, null=False, blank=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + ' - ' + self.school.name

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    semester = models.IntegerField()
    code = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name + ' - ' + self.program.name + ' - ' + self.program.school.name