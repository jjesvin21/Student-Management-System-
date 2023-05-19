from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=200)

class Roles(models.Model):
    role_name = models.CharField(max_length=200)
    
class RolesPermission(models.Model):
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    permission  = models.ForeignKey(Permission,on_delete=models.CASCADE)

class UserRole(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)

class Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
class Teacher(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)