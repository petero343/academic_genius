import random
import string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from teachers.models import Teacher

User = get_user_model()

def generate_random_password(length=8):
    """Generate a random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

@receiver(post_save, sender=Teacher)
def create_teacher_account(sender, instance, created, **kwargs):
    if created:
        random_password = generate_random_password()  # Generate a temporary password
        user, created = User.objects.get_or_create(
             username=instance.id_number,  # Use ID as username
             defaults={
                "email": instance.email,
                "first_name": instance.first_name,
                "last_name": instance.last_name,
                 "role": "teacher",
                 "is_staff": True,  # Give staff access if needed
            }
       )

        # Set temporary password and enforce reset
   #      user.set_password(random_password)
     #    user.password_reset_required = True  # Custom field to enforce reset
       #  user.save()

        # Send email with login details (If SMTP is configured)
        # Send email with login details (If SMTP is configured)
        # Send email with login details (If SMTP is configured)
     #     if settings.EMAIL_HOST_USER:
      #        send_mail(
               #       subject="Your Teacher Account Details",
       #           subject="Your Teacher Account Details",
                #      message=f"Hello {instance.first_name},\n\nYour teacher account has been created.\n\n"
       #                   f"Username: {instance.id_number}\nPassword: {random_password}\n\n"
                      #  "Please log in and change your password immediately.",
             #         from_email=settings.DEFAULT_FROM_EMAIL,
             #         recipient_list=[instance.email],
             #         fail_silently=False,
            #      )
