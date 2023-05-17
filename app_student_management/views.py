from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from app_student_management.models import Roles,UserRole,RolePermition,permition,Student,Teacher
from app_student_management.serializer import Add_Permition_Serializer,Add_Role_Serializer,Role_Permition_Update_Serializer
from app_student_management import serializer
from rest_framework.permissions import IsAuthenticated
from app_student_management.Auths import View_My_Mark_Authentication,Add_Marks_Authentication
# Create your views here.




class Permition(generics.ListCreateAPIView):

    queryset = permition.objects.all()
    serializer_class = Add_Permition_Serializer

    def post(self,request):
        data = request.data
        serializer = Add_Permition_Serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"permition saved ......"})
        return Response({"msg":"Permition not able to save !!!"})
    

class Delete_Permition(APIView):

    def delete(self,request,id):
        
        try:
            id = id
            per = permition.objects.get(id = id)
            if per:
                per.delete()
                return Response({"msg":"Permission deleted sucessfully"})
            return Response({"msg":"Permition is not able to delete"})
        except Exception as e:
            return Response({"msg":"Permition is not able to delete[does not exixt]"})



from app_student_management.serializer import Get_Role_Serializer

class CreateRole(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = Get_Role_Serializer

    def post(self,request):
        data = request.data
        serializer = Add_Role_Serializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Role added"})
        return Response({"msg":"Role cant be sent"})


class Update_Role_Permition(generics.ListCreateAPIView):

    def post(self,request):

        try:
            data = request.data
            sirializer = Role_Permition_Update_Serializer(data = data)
            if sirializer.is_valid():
                sirializer.save()
                return Response({"msg":"permitions updated"})
            return Response({"msg":"permitions can not be updated"})
        except Exception as e:
            return Response({"msg":"Not able to find the responce"})
    
class DeleteRole(APIView):

    def delete(self,request,id):

        role = Roles.objects.get(id=id)
        if role:
            role.delete()
            return Response({"msg":"The Role deleted...."})
        return Response({"msg":"the role is note able to delete"})
    


    
class AddUser(APIView):

    def post(self,request):
        data = request.data
        seri = serializer.Add_User_Serializer(data = data)
        if seri.is_valid():
            seri.save()
            return Response({"msg":"new user added"})
        return Response({"msg":"New User can not be added"})
        
class View_My_Mark(APIView):
     
    permission_classes=[IsAuthenticated,View_My_Mark_Authentication]
     
    def get(self,request):
         return Response({"msg":"you can see your mark"})
    
    


    
class AddMark(APIView):

    permission_classes = [IsAuthenticated,Add_Marks_Authentication]

    def post(self,request):

        data = request.data
        seri = serializer.AddMark_Serializer(data = data)
        if seri.is_valid():
            seri.save()
            return Response({"msg":"Mark added"})
        return Response({"msg":"Message canot be added"})

