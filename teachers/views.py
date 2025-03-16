from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .models import Teacher
from students.models import Student, Result, Course


# ✅ Helper function to check if user is a teacher
def is_teacher(user):
    return user.is_authenticated and hasattr(user, 'teacher')


# ✅ Teacher Login
def teacher_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        print(f"DEBUG: Trying to authenticate {username}")  # Debugging

        user = authenticate(request, username=username, password=password)

        if user:
            print("✅ User authenticated!")  # Debugging

            login(request, user)  # ✅ Log in the user
            return redirect("teacher_dashboard")
        else:
            print("❌ Authentication failed!")  # Debugging
            messages.error(request, "Invalid username or password.")

    return render(request, "teachers/login.html")

# ✅ Teacher Logout
def teacher_logout(request):
    logout(request)
    return redirect("teacher_login")


# ✅ Force Teacher to Reset Password on First Login
@login_required
def teacher_password_reset(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            user.teacher.password_reset_required = False  # Remove reset flag
            user.teacher.save()
            update_session_auth_hash(request, user)  # Prevent logout after password change
            messages.success(request, "Your password has been changed successfully.")
            return redirect("teacher_dashboard")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "teachers/password_reset.html", {"form": form})


# ✅ Teacher Dashboard
@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    teacher = request.user.teacher  # Get the logged-in teacher
    assigned_subjects = teacher.assigned_subjects.all()
    students = Student.objects.filter(result__course__in=assigned_subjects).distinct()

    context = {
        "teacher": teacher,
        "assigned_subjects": assigned_subjects,
        "students": students,
    }
    return render(request, "teachers/dashboard.html", context)


# ✅ Teacher Profile & Assign Subjects
@login_required
@user_passes_test(is_teacher)
def teacher_profile(request):
    teacher = request.user.teacher  # Get the logged-in teacher
    all_courses = Course.objects.all()  # Fetch all subjects

    if request.method == "POST":
        selected_courses = request.POST.getlist("assigned_subjects")
        teacher.assigned_subjects.set(selected_courses)  # Assign subjects
        teacher.save()
        messages.success(request, "Subjects updated successfully.")
        return redirect("teacher_profile")  # Refresh page

    return render(request, "teachers/profile.html", {"teacher": teacher, "all_courses": all_courses})


# ✅ Teachers Can View Their Students' Results
@login_required
@user_passes_test(is_teacher)
def teacher_view_results(request):
    teacher = request.user.teacher
    assigned_subjects = teacher.assigned_subjects.all()
    students = Student.objects.filter(result__course__in=assigned_subjects).distinct()

    context = {
        "teacher": teacher,
        "students": students,
        "assigned_subjects": assigned_subjects,
    }
    return render(request, "teachers/view_results.html", context)


# ✅ Teachers Can Add & Edit Student Results
@login_required
@user_passes_test(is_teacher)
def teacher_add_results(request):
    teacher = request.user.teacher
    assigned_subjects = teacher.assigned_subjects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        course_id = request.POST.get("course_id")
        grade = request.POST.get("grade")

        student = get_object_or_404(Student, id=student_id)
        course = get_object_or_404(Course, id=course_id)

        if course in assigned_subjects:
            result, created = Result.objects.update_or_create(
                student=student, course=course, defaults={"grade": grade}
            )
            messages.success(request, "Result updated successfully.")
        else:
            messages.error(request, "You can only assign results for your assigned subjects.")

    students = Student.objects.filter(result__course__in=assigned_subjects).distinct()

    return render(
        request, "teachers/add_results.html",
        {"teacher": teacher, "students": students, "assigned_subjects": assigned_subjects}
    )
