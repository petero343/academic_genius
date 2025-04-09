from django.urls import path
from .views import (
    teacher_login,
    teacher_dashboard,
    teacher_logout,
    teacher_students,              # Renamed from view_students
    teacher_add_student_results,   # For adding results for a specific student
    teacher_edit_result,           # For editing a result
    teacher_list,
    teacher_results,
    teacher_manage_results,
    teacher_profile
)

urlpatterns = [
    path("login/", teacher_login, name="teacher_login"),
    path("dashboard/", teacher_dashboard, name="teacher_dashboard"),
    path("logout/", teacher_logout, name="teacher_logout"),
    path("students/", teacher_students, name="teacher_students"),
    path("students/<int:student_id>/add_results/", teacher_add_student_results, name="add_results"),
    path("results/<int:result_id>/edit/", teacher_edit_result, name="edit_result"),
    path("list/", teacher_list, name="teacher_list"),
    path("results/", teacher_results, name="teacher_results"),
    path("manage_results/", teacher_manage_results, name="teacher_manage_results"),
    path("profile/", teacher_profile, name="teacher_profile"),
]
