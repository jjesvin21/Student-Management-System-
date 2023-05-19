from  rest_framework import serializers
from app.student_app.models import Permission,Roles,RolesPermission
from app.student_app.models import Student,Teacher,UserRole
from django.contrib.auth.models import User


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        
class RolesGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class RolesAddSerializer(serializers.ModelSerializer):
    permissions = serializers.ListField()
    class Meta:
        model = Roles
        fields = ['role_name','permissions']
        read_only_fields = ['permissions']
    
    def create(self, validated_data):
        
        role_name = validated_data['role_name']
        permissions = validated_data['permissions']

        roles = Roles(role_name = role_name)
        roles.save()

        print(permissions)
        for item in permissions:
            try:
                per = Permission.objects.get(id = item)
                rolespermission = RolesPermission(role = roles,permission = per)
                print(rolespermission)
                rolespermission.save()
            except Exception as e:
                print("does not exist")
                return {"msg":"permission not found"}
            
    
        return roles
            
class RolePermissionUpdateSerializer(serializers.ModelSerializer):
    roleid = serializers.IntegerField()
    permissions = serializers.ListField()
    class Meta:
        model = RolesPermission
        fields = ['roleid','permissions']
        read_only_fields = ['roleid','permissions']
    
    def create(self, validated_data):
        try:
            roleid = validated_data['roleid']
            permissions = validated_data['permissions']

            role = Roles.objects.get(id=roleid)
            rolepermission = RolesPermission.objects.filter(role = role)
            rolepermission.delete()

            for item in permissions:
                per = Permission.objects.get(id=item)
                rolepermission = RolesPermission(role = role,permission = per)
                rolepermission.save()
        except Exception as e:
            return e
        return rolepermission
class GetAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class StudentAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
    
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']

        user = User(first_name=first_name,last_name=last_name,email=email,username = username)
        user.set_password(password)
        user.save()
        student = Student(student = user)
        student.save()
        role = Roles.objects.get(role_name = 'student')
        userrole = UserRole(user = user,role = role)
        userrole.save()
        return user
    


class TeacherAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
    
    def create(self, validated_data):

        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']

        user = User(first_name=first_name,last_name=last_name,email=email,username = username)
        user.set_password(password)
        user.save()
        teacher = Teacher(teacher = user)
        teacher.save()
        role = Roles.objects.get(role_name = 'teacher')
        userrole = UserRole(user = user,role = role)
        userrole.save()
        return user
