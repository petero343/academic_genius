# students/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_results_notification(student):
    """Send an email notification to a student when results are available."""
    subject = "Your New Exam Results Are Available!"
    message = f"""
    Hello {student.first_name},

    Your new results are now available on the student portal.
    
    Login to your account to view your performance.

    Regards,
    Shiners Academy
    """
    recipient = student.user.email  # ✅ Ensure student has an associated CustomUser

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])
