from django.urls import path
from . import views

urlpatterns = [
    path('', views.goods_list, name="goods_list"),
    path('goods/add/', views.goods_add, name="goods_add"),
    path('goods/detail/<int:id>/', views.goods_detail, name="goods_detail"),
    path('goods/edit/<int:id>/', views.goods_edit, name="goods_edit"),
    path('goods/delete/<int:id>/', views.goods_delete, name="goods_delete"),

    path('student/list/', views.student_list, name="student_list"),
    path('student/add/', views.student_add, name="student_add"),
    path('student/edit/<int:pk>/', views.student_edit, name="student_edit"),
    path('student/delete/<int:pk>/', views.student_delete, name="student_delete"),
]