from django.contrib import admin
from django.urls import path, include
from students.views import home
from users.views import custom_admin_login
urlpatterns = [
    # ✅ Admin Panel
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # ✅ Ensure auth URLs are included

    path("", home, name="home"),
    # ✅ Student URLs
    path("students/", include("students.urls")),  # ✅ Ensure students URLs are included

    path('admin/login/', custom_admin_login, name='custom_admin_login'),

    # ✅ Teacher URLs
    path("teachers/", include("teachers.urls")),

    path('', include('users.urls')),  # Include users app URLs

]
