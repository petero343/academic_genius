from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models

# ✅ Custom Manager for Teachers
class TeacherManager(BaseUserManager):
    def create_user(self, id_number, password=None, **extra_fields):
        """Create and return a regular teacher."""
        if not id_number:
            raise ValueError("The ID number is required")
        extra_fields.setdefault("is_active", True)  # Ensure active by default
        teacher = self.model(id_number=id_number, **extra_fields)
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

    def create_superuser(self, id_number, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(id_number, password, **extra_fields)

# ✅ Custom Teacher Model (AUTH_USER_MODEL)
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    assigned_subjects = models.ManyToManyField('Course')
    date_joined = models.DateTimeField(auto_now_add=True)


    # ✅ Permissions
    groups = models.ManyToManyField(Group, related_name="teacher_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="teacher_permissions", blank=True)

    # ✅ Define custom manager
    objects = TeacherManager()

    USERNAME_FIELD = "id_number"  # Teachers log in with ID number
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_number})"

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name