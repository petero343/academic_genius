from django.urls import path
from .views import (
    student_list, student_detail, generate_report_card, generate_results_report, 
    student_login, student_dashboard, view_results, user_logout, home
)

#app_name = "students"

urlpatterns = [
    # ✅ Home & Authentication
    path("", home, name="home"),
    path("login/", student_login, name="student_login"),
    path("logout/", user_logout, name="user_logout"),
    
    # ✅ Student Dashboard
    path("dashboard/", student_dashboard, name="student_dashboard"),  

    # ✅ Student Management
    path("students/", student_list, name="student_list"),  # ✅ Fix duplicate empty path
    path("students/<str:adm_number>/", student_detail, name="student_detail"),

    # ✅ Reports & Results
    path("students/<str:adm_number>/report/", generate_report_card, name="generate_report_card"),
    path("students/<str:adm_number>/results/", generate_results_report, name="generate_results_report"),
    path("results/", view_results, name="view_results"),
]
