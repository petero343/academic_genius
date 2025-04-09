from django.urls import path
from .views import (
    admin_dashboard, admin_login, admin_logout, 
    manage_teachers, add_teacher, edit_teacher, delete_teacher,
    manage_students, add_student, edit_student, delete_student,  # ✅ Added student routes
    manage_courses, add_course, edit_course, delete_course  # ✅ Added course routes
)

urlpatterns = [
    path("admin/dashboard/", admin_dashboard, name="custom_admin_dashboard"),
    path("admin/login/", admin_login, name="custom_admin_login"),
    path("admin/logout/", admin_logout, name="custom_admin_logout"),
    
    # ✅ Teachers Management
    path("admin/teachers/", manage_teachers, name="manage_teachers"),
    path("admin/teachers/add/", add_teacher, name="admin_add_teacher"),
    path("admin/teachers/edit/<int:teacher_id>/", edit_teacher, name="admin_edit_teacher"),
    path("admin/teachers/delete/<int:teacher_id>/", delete_teacher, name="admin_delete_teacher"),
    
    # ✅ Students Management
    path("admin/students/", manage_students, name="manage_students"),
    path("admin/students/add/", add_student, name="admin_add_student"),
    path("admin/students/edit/<int:student_id>/", edit_student, name="admin_edit_student"),
    path("admin/students/delete/<int:student_id>/", delete_student, name="admin_delete_student"),

    # ✅ Courses Management
    path("admin/courses/", manage_courses, name="manage_courses"),
    path("admin/courses/add/", add_course, name="add_course"),
    path("admin/courses/edit/<int:course_id>/", edit_course, name="admin_edit_course"),
    path("admin/courses/delete/<int:course_id>/", delete_course, name="admin_delete_course"),
]
