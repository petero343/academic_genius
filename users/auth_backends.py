from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)  # Fetch by username (Admission Number)
            if user.check_password(password):  # Check hashed password
                return user
        except CustomUser.DoesNotExist:
            return None
