from django.urls import path
from .views import teacher_login, teacher_logout, teacher_dashboard

urlpatterns = [
    path("login/", teacher_login, name="teacher_login"),
    path("logout/", teacher_logout, name="teacher_logout"),
    path("dashboard/", teacher_dashboard, name="teacher_dashboard"),  # ✅ Fixed
]
