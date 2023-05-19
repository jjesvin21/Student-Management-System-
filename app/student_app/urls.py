from django.urls import path
from app.student_app import views

urlpatterns = [
    path("",views.Hello.as_view()),
    path("permission/",views.Permission.as_view()),
    path("permission/<int:id>/",views.PermitionDelete.as_view()),
    path("roles/",views.RoleCreation.as_view()),
    path("roles/<int:id>/",views.RoleDelete.as_view()),
    path("student/",views.Students.as_view()),
]