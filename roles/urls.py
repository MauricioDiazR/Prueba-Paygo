from django.urls import path
from roles import views

urlpatterns = [
    path ('permissions/', views.PermissionList.as_view()),
    path ('permissions/<int:pk>/', views.PermissionDetail.as_view()),
    path ('roles/', views.RoleList.as_view()),
    path ('roles/<int:pk>/', views.RoleDetail.as_view()),
    path ('users/',views.UserList.as_view()),
    path ('users/<int:pk>/', views.UserDetail.as_view())

]