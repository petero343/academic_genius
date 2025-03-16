from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue, black, red, lightgrey
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import os
from django.conf import settings

from .models import Student, Result, Course


# ✅ List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


# ✅ View individual student details
def student_detail(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)
    return render(request, 'students/student_detail.html', {'student': student})


# ✅ Generate PDF Report Card
def generate_report_card(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Report_Card_{student.adm_number}.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 16)
    p.drawString(100, 800, "Student Report Card")
    p.setFont("Helvetica", 12)
    p.drawString(100, 780, f"Name: {student.first_name} {student.last_name}")
    p.drawString(100, 760, f"Admission Number: {student.adm_number}")
    p.drawString(100, 740, f"Email: {student.email}")
    p.drawString(100, 720, f"Date of Birth: {student.dob}")
    p.drawString(100, 700, f"Age: {student.calculate_age()}")

    p.showPage()
    p.save()

    return response


# ✅ Generate Student Results PDF
def generate_results_report(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)
    results = Result.objects.filter(student=student)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Results_{student.adm_number}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # 🏫 **School Logo**
    logo_path = os.path.join(settings.BASE_DIR, "students/static/images/logo.png")  
    if os.path.exists(logo_path):
        p.drawImage(ImageReader(logo_path), width / 2 - 50, height - 100, width=100, height=100)

    # 🎯 **Title Section**
    p.setFillColor(lightgrey)
    p.rect(50, height - 136, width - 70, 40, fill=True, stroke=False)
    p.setFillColor(blue)
    p.setFont("Helvetica-Bold", 20)
    p.drawString(180, height - 120, "Student Results Report")

    # ✍️ **Student Details**
    p.setFillColor(black)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 160, "Student Information:")
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 180, f"Name: {student.first_name} {student.last_name}")
    p.drawString(100, height - 200, f"Admission Number: {student.adm_number}")

    # 📚 **Results Table Header**
    p.setFont("Helvetica-Bold", 14)
    p.setFillColor(red)
    p.drawString(100, height - 230, "Results:")

    # 📝 **Prepare Table Data**
    table_data = [["Course", "Grade"]]  # Table Headers
    for result in results:
        table_data.append([result.course.name, result.grade])

    if not results:
        table_data.append(["No results available", "—"])

    # ✏️ **Table Style**
    table = Table(table_data, colWidths=[300, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # 📌 **Draw Table**
    table.wrapOn(p, width, height)
    table.drawOn(p, 100, height - 280)

    # 🔚 **Close PDF document**
    p.showPage()
    p.save()

    return response


# ✅ Student Dashboard
@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, adm_number=request.user.username)
    results = Result.objects.filter(student=student)

    subjects = [result.course.name for result in results]  
    grades = [int(result.grade) for result in results] if results else []

    context = {
        "student": student,
        "results": results,
        "subjects": subjects,
        "grades": grades,
    }
    return render(request, "students/dashboard.html", context)


# ✅ Student Login
def student_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and hasattr(user, 'student'):  # Ensure it's a student
            login(request, user)
            return redirect("student_dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "students/login.html")


# ✅ User Logout
def user_logout(request):
    logout(request)
    return redirect("student_login")


# ✅ Helper function to check if user is an admin
def is_admin(user):
    return user.is_authenticated and user.role == "admin"


# ✅ Helper function to check if user is a teacher
def is_teacher(user):
    return user.is_authenticated and user.role == "teacher"


# ✅ Helper function to check if user is a student or parent
def is_student_or_parent(user):
    return user.is_authenticated and user.role in ["student", "parent"]


# ✅ Admin-only view (Manage students)
@login_required
@user_passes_test(is_admin)
def manage_students(request):
    students = Student.objects.all()
    return render(request, "students/manage_students.html", {"students": students})


# ✅ Teachers can add/edit results
@login_required
@user_passes_test(is_teacher)
def add_results(request):
    return render(request, "students/add_results.html")


# ✅ Students/Parents can only view their own results
@login_required
@user_passes_test(is_student_or_parent)
def view_results(request):
    student = get_object_or_404(Student, user=request.user)
    results = Result.objects.filter(student=student)
    return render(request, "students/view_results.html", {"student": student, "results": results})
