from django.db import models
from django.contrib.auth.models import Group, Permission
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import date  # ✅ Import date for age calculation
# Removed the User variable assignment to use settings.AUTH_USER_MODEL directly
from django.contrib.auth import get_user_model
User = get_user_model()  # ✅ Correct way to reference User model


from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from datetime import date
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

class Student(models.Model):
    adm_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()  # ✅ Only one dob field
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    class_grade = models.CharField(max_length=10)
    guardian_contact = PhoneNumberField()

    def age(self):
        """Calculate age based on DOB"""
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    age.short_description = "Age"

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

def save(self, *args, **kwargs):
    User = get_user_model()  # ✅ Get the correct user model

    if not self.user:  # ✅ Only create a user if one does not exist
        user, created = User.objects.get_or_create(
            username=self.adm_number,  # ✅ Username = Admission Number
            defaults={
                "email": f"{self.adm_number}@shinersacademy.com",
                "password": "password123",  # ✅ Default password
            }
        )
        self.user = user  # ✅ Assign the user to the student

    if self.user:
        # ✅ Ensure the user is in the "Students" group
        student_group, _ = Group.objects.get_or_create(name="Students")
        self.user.groups.add(student_group)

        self.user.is_active = True  # ✅ Ensure account is active
        self.user.save()

    super().save(*args, **kwargs)  # ✅ Save student instance

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.code})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)  # Set a temporary default
    grade = models.CharField(max_length=2, blank=True, null=True)  # Allow null/blank for grade initially
    
    def save(self, *args, **kwargs):
        # Convert marks to int if it's a string
        try:
            self.marks = int(self.marks)
            print(f"Marks after conversion: {self.marks}")
        except (ValueError, TypeError):
            raise ValueError("Marks must be aa valid integer.")

        # Validate that marks are between 0 and 100
        if self.marks < 0 or self.marks > 100:
            raise ValueError(f"Marks {self.marks} must be between 0 and 100.")
        
        # Log to check grade assignment flow
        print(f"Grade before assignment: {self.grade}")
        
        # Reset the grade to None (if needed)
        self.grade = None
        
        # Automatically assign grade based on marks
        if self.marks >= 80:
            self.grade = "A"
        elif self.marks >= 70:
            self.grade = "B"
        elif self.marks >= 60:
            self.grade = "C"
        elif self.marks >= 50:
            self.grade = "D"
        else:
            self.grade = "E"
        
        print(f"Assigned grade: {self.grade}")
        
        super().save(*args, **kwargs)
