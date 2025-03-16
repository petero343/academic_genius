from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ✅ Admin Panel
    path("admin/", admin.site.urls),

    # ✅ Home Page
    path("", include("students.urls")),  # Home handled in students

    # ✅ Student URLs
    path("students/", include("students.urls")),

    # ✅ Teacher URLs
    path("teachers/", include("teachers.urls")),
]
