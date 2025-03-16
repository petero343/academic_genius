from django.urls import path
from .views import (
    student_list, student_detail, generate_report_card, generate_results_report, 
    student_login, student_dashboard, view_results, user_logout
)

urlpatterns = [
    # ✅ Student Login & Dashboard
    path("login/", student_login, name="student_login"),
    path("dashboard/", student_dashboard, name="student_dashboard"),

    # ✅ Student List & Details
    path("", student_list, name="student_list"),
    path("<str:adm_number>/", student_detail, name="student_detail"),

    # ✅ Report & Results
    path("<str:adm_number>/report/", generate_report_card, name="generate_report_card"),
    path("<str:adm_number>/results/", generate_results_report, name="generate_results_report"),
    path("results/", view_results, name="view_results"),

    # ✅ Logout
    path("logout/", user_logout, name="user_logout"),
]
