
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('register/', views.register, name='register' ),
    path('logout/', views.MyLogoutView.as_view(), name='logout' ),
    path('profile/', views.profile, name='profile' ),
    path('groups/', views.groups, name='groups' ),
    path('leave/<int:id>', views.leave_from_group, name='leave' ),
    path('add/<int:id>', views.add_to_group, name='add_to_group' ),
    path('users/', views.users, name='users' ),
    path('change_group/', views.change_group, name='change_group' ),

]
