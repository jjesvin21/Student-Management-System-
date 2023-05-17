from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Roles(models.Model):
    role = models.CharField(max_length=100)

class UserRole(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)

class permition(models.Model):
    name = models.CharField(max_length=100)

class RolePermition(models.Model):
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    permition = models.ForeignKey(permition,on_delete=models.CASCADE)



    
class Marks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    physics = models.IntegerField()
    maths = models.IntegerField()
    chem = models.IntegerField()
    total = models.IntegerField()

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100,unique=True)

class Teacher(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)

class Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)

class TeacherCourse(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

class StudentCourse(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course  = models.ForeignKey(Course,on_delete=models.ForeignKey)




