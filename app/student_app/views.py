from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.student_app import services
# Create your views here.

class Hello(APIView):
    def get(self,request):
        return Response({"msg":"This is a Student Management App"})

class Permission(APIView):
    def get(self,request):
        res = services.getallpermissions(request=request)
        return Response(res)    
    def post(self,request):
        res = services.addpermission(request=request)
        return Response(res)
    
class PermitionDelete(APIView):
    def delete(self,request,id):
        res = services.deletePermission(request=request,id=id)
        return Response(res)

class RoleCreation(APIView):
    def get(self,request):
        res = services.getallRoles(request=request)
        return Response(res)
    def post(self,request):
        res = services.createRole(request=request)
        return Response(res)
    def put(self,request):
        res = services.updateRole(request=request)
        return Response(res)
    
class RoleDelete(APIView):
    def delete(self,request,id):
        res = services.deleteRole(request=request,id=id)
        return Response(res)
    
class Students(APIView):
    def get(self,request):
        res=services.getallStudents(request=request)
        return Response(res)
    
    def post(self,request):
        res = services.addStudent(request=request)
        return Response(res)
    
        