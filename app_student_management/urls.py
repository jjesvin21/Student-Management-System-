from django.urls import path ,include
from rest_framework_simplejwt import views as jwt_views
from app_student_management import views
from app_student_management import Auths
urlpatterns = [
    path('Permition/',views.Permition.as_view()),
    path('Permition/<int:id>/',views.Delete_Permition.as_view()),    
    path('createrole/',views.CreateRole.as_view()),
    path('updaterolepermition/',views.Update_Role_Permition.as_view()),
    path('deleterole/<int:id>/',views.DeleteRole.as_view()),

    
    path("token/",jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('mymarks/',views.View_My_Mark.as_view()),
    path('addmarks/',views.AddMark.as_view()),
    path('addnewuser/',views.AddUser.as_view()),


]
