from django.urls import path
from .views import (
    teacher_login, teacher_dashboard, teacher_logout,
    view_students, add_results, edit_results
)

urlpatterns = [
    path("login/", teacher_login, name="teacher_login"),
    path("dashboard/", teacher_dashboard, name="teacher_dashboard"),
    path("logout/", teacher_logout, name="teacher_logout"),
    path("students/", view_students, name="view_students"),
    path("students/<int:student_id>/add_results/", add_results, name="add_results"),
    path("results/<int:result_id>/edit/", edit_results, name="edit_results"),
]
