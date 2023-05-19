from app.student_app.serializers import PermissionsSerializer,RolesAddSerializer
from app.student_app.models import Permission,Roles,RolesPermission
from app.student_app.models import Student,Teacher,UserRole
from app.student_app.serializers import RolePermissionUpdateSerializer
from app.student_app.serializers import RolesGetSerializer
from app.student_app.serializers import GetAllUserSerializer,StudentAddSerializer

from django.contrib.auth.models import User


def addpermission(request):
    data = request.data
    serializer = PermissionsSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return {"msg":"Permission added"}
    return {"msg":"Permission can't be added"}

def deletePermission(request,id):
    id= id
    try:
        permission = Permission.objects.get(id = id)
        if permission:
            permission.delete()
            return {"msg":"permission deleted sucessfully"}
        return {"mag":"permission can not be deleted "}
    except Exception as e:
        return {"msg":"permission can not be deleted "}   

def getallpermissions(request):
    quriset = Permission.objects.all()
    serializer = PermissionsSerializer(quriset,many = True)
    return serializer.data

def createRole(request):
    data = request.data
    serializer = RolesAddSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {"msg":"Role sucessfully created"}
    return {"msg":"Role con not be created"}

def deleteRole(request,id):
    try:
        id = id
        role = Roles.objects.get(id=id)
        if role:
            role.delete()
            return {"msg":"Role deleted sucessfully"}
        return {"msg":"Role not able to delete"}
    except Exception as e:
        return {"msg":"Role not able to delete"}

def updateRole(request):
    data = request.data
    serializer = RolePermissionUpdateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {"msg":"Role updated sucessfully"}
    return {"msg":"Role can not be updated"}

def getallRoles(request):
    quriset = Roles.objects.all()
    serializer = RolesGetSerializer(quriset,many=True)
    return serializer.data

def getallStudents(request):
    quriset  = User.objects.filter(id__in=Student.objects.values('student_id'))
    serializer = GetAllUserSerializer(quriset,many=True)
    return serializer.data

def addStudent(request):
    data = request.data
    serializer  = StudentAddSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {"msg":"Student added"}
    return {"msg":"Student can not be added"}



def getallTeachers(request):
    quriset  = User.objects.filter(id__in=Teacher.objects.values('teacher_id'))
    serializer = GetAllUserSerializer(quriset,many=True)
    return serializer.data

