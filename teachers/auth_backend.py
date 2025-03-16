from django.contrib.auth.backends import ModelBackend
from teachers.models import Teacher

class TeacherAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            teacher = Teacher.objects.get(id_number=username)  # Use id_number as username
            if teacher.check_password(password):  # Check password
                return teacher
        except Teacher.DoesNotExist:
            return None

