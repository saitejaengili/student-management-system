from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("students/add/", views.student_create, name="student_add"),
    path("students/<int:pk>/edit/", views.student_update, name="student_edit"),
    path("students/<int:pk>/delete/", views.student_delete, name="student_delete"),
]
