from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.conf import settings

class Student(models.Model):
    adm_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # ✅ Automatically create a user account
        user, created = User.objects.get_or_create(username=self.adm_number, defaults={
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        })

        if created:
            user.set_password("password123")  # 🔐 Default password (change later)
            user.save()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.adm_number}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.code})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"

