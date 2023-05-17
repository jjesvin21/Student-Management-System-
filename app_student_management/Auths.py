
from django.contrib.auth.models import User
from rest_framework import permissions
from app_student_management.models import Roles,UserRole,RolePermition,permition


class View_My_Mark_Authentication(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            print(user)
            userrole = UserRole.objects.get(user = user)
            print(userrole)
            role = userrole.role
            per = permition.objects.get(name = "view_my_mark")
            if RolePermition.objects.filter(role=role,permition = per).exists():
                return True
            return False
           
        except Exception as e:
            return False
    
class Add_Marks_Authentication(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            userrole = UserRole.objects.get(user = user)
            role = userrole.role
            per = permition.objects.get(name = 'add_mark')
            if RolePermition.objects.filter(role = role,permition = per).exists():
                return True
            return False
        except Exception as e:
            return False
        

class CURD_Permition_Authentication(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            user = request.user
            userrole = UserRole.objects.get(user = user)
            role = userrole.role
            per = permition.objects.get(name = 'add_permition')
            if RolePermition.objects.filter(role = role,permition = per).exists():
                return True
            return False

        except Exception as e:
            return False

class CURD_Role_Authentication(permissions.BasePermission):
   
   def has_permission(self, request, view):
        try:
            user = request.user
            userrole = UserRole.objects.get(user = user)
            role = userrole.role
            per = permition.objects.get(name = 'CURD_roles')
            if RolePermition.objects.filter(role = role,permition = per).exists():
                return True
            return False

        except Exception as e:
            return False
        
class CURD_Teacher_Authentication(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            userrole = UserRole.objects.get(user = user)
            role = userrole.role
            per = permition.objects.get(name = 'CURD_teacher')
            if RolePermition.objects.filter(role = role, permissions = per).exists():
                return True
            return False
        except Exception as e:
            return False
        
class CURD_Student_Authentication(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            userrole = UserRole.objects.get(user = user)
            role = userrole.role
            per = permition.objects.get(name = 'CURD_student')
            if RolePermition.objects.filter(role = role, permissions = per).exists():
                return True
            return False
        except Exception as e:
            return False
        

