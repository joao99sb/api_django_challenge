from django.db import models
from db_connections import db 

# Create your models here.
character_connection = db['Character']
book_connection = db['Book']

# class Departments(models.Model):
#     DepartmentId = models.AutoField(primary_key=True)
#     DepartmentName = models.CharField(max_length=500)

# class Employees(models.Model):
#     EmployeeId = models.AutoField(primary_key=True)
#     EmployeeName = models.CharField(max_length=500)
#     Department = models.CharField(max_length=500)
#     DateOfJoining = models.DateField()
#     PhotoFileName = models.CharField(max_length=500)