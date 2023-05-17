from rest_framework import serializers
from django.contrib.auth.models import User

from app_student_management.models import Roles,UserRole,RolePermition,permition,Marks,Student,Teacher


class Teacher_Add_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fielda = ['username','password','first_name','last_name','email']
    
    def create(self, validated_data):
        
        email = validated_data['email']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']

        user = User(username = username, email = email , first_name = first_name , last_name = last_name)
        user.set_password(password)
        user.save()

        
class Add_Permition_Serializer(serializers.ModelSerializer):
    class Meta:
        model = permition
        fields = '__all__'

class Get_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class Add_Role_Serializer(serializers.ModelSerializer):

    permitions = serializers.ListField()

    class Meta:
        model = Roles
        fields = ['role','permitions']
        read_only_fields = ['permitions']

    def create(self, validated_data):
        
        permitions = validated_data['permitions']
        role = validated_data['role']

        roles = Roles(role = role)
        roles.save()

        for permition_item in permitions:
            per = permition.objects.get(id = permition_item)
            role_permition = RolePermition(role = roles,permition = per )
            role_permition.save()
        
        return roles

class Role_Permition_Update_Serializer(serializers.ModelSerializer):
    
    permitions = serializers.ListField()
    roleid = serializers.IntegerField()

    class Meta:
        model = RolePermition
        fields = ['roleid','permitions']
        read_only_fields = ['permitions','roleid']
    
    def create(self, validated_data):
        roleid = validated_data['roleid']
        permitions = validated_data['permitions']
        role = Roles.objects.get(id = roleid)

        rolepermition  = RolePermition.objects.filter(role=role)
        rolepermition.delete()

        for permitions_item in permitions:
            per = permition.objects.get(id=permitions_item)
            newrolepermition = RolePermition(role = role , permition = per)
            newrolepermition.save()
        return newrolepermition

class get_student_list(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Add_User_Serializer(serializers.ModelSerializer):

    roleid = serializers.IntegerField()
    class  Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','roleid']
        read_only_fields = ['roleid']
    
    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        password = validated_data['password']
        roleid = validated_data['roleid']

        user = User(email=email,username=username,first_name=first_name,last_name=last_name)
        user.set_password(password)

        user.save()

        role = Roles.objects.get(id=roleid)
        userrole = UserRole(role = role, user = user)
        userrole.save()

        return user


class AddMark_Serializer(serializers.ModelSerializer):
    userid = serializers.IntegerField()
    class Meta:
        model = Marks
        fields = ['physics','maths','chem','userid']
        read_only_field = ['userid']
    
    def create(self, validated_data):
        
        physics = validated_data['physics']
        maths = validated_data['maths']
        chem = validated_data['chem']
        total = physics+chem+maths
        userid = validated_data['userid']

        user = User.objects.get(id=userid)
        mark = Marks(user=user,physics = physics,chem = chem,maths = maths,total = total)
        mark.save()
        return mark
