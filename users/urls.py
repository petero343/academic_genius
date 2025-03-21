from django.urls import path
from .views import custom_admin_login

urlpatterns = [
    path('admin/login/', custom_admin_login, name='custom_admin_login'),
]
