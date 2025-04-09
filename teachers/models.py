from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models
from users.models import CustomUser

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
    assigned_subjects = models.ManyToManyField("students.Course")
    date_joined = models.DateField(auto_now_add=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        """ Automatically create a user account for a teacher upon saving. """
        creating = self._state.adding  # Check if it's a new teacher
        super().save(*args, **kwargs)

        if creating:
            # ✅ Create a linked user account
            user, created = CustomUser.objects.get_or_create(
                username=self.id_number,  # Use ID as the username
                defaults={
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "email": self.email,
                    "role": "teacher",
                },
            )
            if created:
                user.set_password("password123")  # Set a default password (Changeable later)
                user.save()
            self.user = user  # Explicitly link the CustomUser instance to the Teacher
            super().save(update_fields=["user"])  # Update the user field in the database

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