from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ✅ Admin Panel
    path("admin/", admin.site.urls),

    # ✅ Home Page

    # ✅ Student URLs
    path("students/", include(("students.urls", "students"))),  # ✅ Namespace defined here

    # ✅ Teacher URLs
    path("teachers/", include("teachers.urls")),
]
