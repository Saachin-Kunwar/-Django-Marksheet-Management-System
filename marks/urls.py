from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='list'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),


    # 🔐 auth routes
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]