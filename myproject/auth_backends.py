from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from students.models import Student
from teachers.models import Teacher

# Get the correct CustomUser model
User = get_user_model()

class CustomUserBackend(ModelBackend):
    """Handles authentication for both students and teachers."""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)  # Query CustomUser instead of User
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
