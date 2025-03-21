from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import blue, black, red, lightgrey
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import os

from users.models import CustomUser
from .models import Student, Result, Course
from .utils import send_results_notification  # ✅ Import function

# ✅ Home View
def home(request):
    return render(request, "students/home.html")

# ✅ Student Login
def student_login(request):
    print("✅ student_login function called!")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            request.session.save()  # ✅ Ensure session is saved
            print(f"✅ Authentication successful! Redirecting {username} to dashboard.")
            return redirect("student_dashboard")  # ✅ No namespaces used
        else:
            messages.error(request, "❌ Invalid username or password")
            print("❌ Authentication failed!")

    return render(request, "students/login.html")

# ✅ Student Dashboard
@login_required(login_url="student_login")
def student_dashboard(request):
    print(f"✅ student_dashboard function called!")
    print(f"✅ Logged-in User: {request.user.username}, Authenticated: {request.user.is_authenticated}")

    student = get_object_or_404(Student, user=request.user)
    results = Result.objects.filter(student=student)

    # Extract subjects and grades for Chart.js
    subjects = [result.course.name for result in results]
    grades = [int(result.grade) for result in results]

    context = {
        "student": student,
        "subjects": subjects,
        "grades": grades,
    }
    return render(request, "students/dashboard.html", context)
# ✅ Logout View
@login_required(login_url="student_login")
def user_logout(request):
    logout(request)
    return redirect("student_login")

# ✅ List all students
@login_required(login_url="student_login")
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})

@login_required
def report_card_preview(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)
    return render(request, "students/report_card_preview.html", {"student": student})

# ✅ Results Preview
@login_required
def results_preview(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)
    results = Result.objects.filter(student=student)
    return render(request, "students/results_preview.html", {"student": student, "results": results})

# ✅ View individual student details
@login_required(login_url="student_login")
def student_detail(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)
    return render(request, "students/student_detail.html", {"student": student})

# ✅ View Results
@login_required(login_url="student_login")
def view_results(request):
    student = get_object_or_404(Student, user=request.user)
    results = Result.objects.filter(student=student)
    return render(request, "students/view_results.html", {"student": student, "results": results})

# ✅ Teachers can add/edit results
@login_required(login_url="student_login")
@user_passes_test(lambda user: user.is_authenticated and user.role == "teacher")
def add_results(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        course = request.POST["course"]
        grade = request.POST["grade"]
        Result.objects.create(student=student, course_id=course, grade=grade)

        send_results_notification(student)  # ✅ Send email notification

        messages.success(request, "Results added successfully!")
        return redirect("teacher_dashboard")  

    return render(request, "students/add_results.html", {"student": student})

# ✅ Generate PDF Report Card
@login_required(login_url="student_login")
def generate_report_card(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="Report_Card_{student.adm_number}.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 16)
    p.drawString(100, 800, "Student Report Card")
    p.setFont("Helvetica", 12)
    p.drawString(100, 780, f"Name: {student.first_name} {student.last_name}")
    p.drawString(100, 760, f"Admission Number: {student.adm_number}")

    p.showPage()
    p.save()
    return response

# ✅ Generate Student Results PDF
@login_required(login_url="student_login")
def generate_results_report(request, adm_number):
    student = get_object_or_404(Student, adm_number=adm_number)
    results = Result.objects.filter(student=student)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="Results_{student.adm_number}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # 🏫 **School Logo**
    logo_path = os.path.join(settings.BASE_DIR, "students/static/images/logo.png")
    if os.path.exists(logo_path):
        p.drawImage(ImageReader(logo_path), width / 2 - 50, height - 100, width=100, height=100)

    # 🎯 **Title Section**
    p.setFillColor(lightgrey)
    p.rect(50, height - 160, width - 70, 40, fill=True, stroke=False)
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
    table_data = [["Course", "Grade"]]
    for result in results:
        table_data.append([result.course.name, result.grade])

    if not results:
        table_data.append(["No results available", "—"])

    # ✏️ **Table Style**
    table = Table(table_data, colWidths=[300, 100])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    # 📌 **Draw Table**
    table.wrapOn(p, width, height)
    table.drawOn(p, 100, height - 280)

    p.showPage()
    p.save()
    return response
