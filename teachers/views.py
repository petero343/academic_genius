from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Avg  
from .forms import ResultForm
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

        print(f"DEBUG: Trying to authenticate {username}")

        user = authenticate(request, username=username, password=password)

        if user:
            print("✅ User authenticated!")
            login(request, user)
            return redirect("teacher_dashboard")
        else:
            print("❌ Authentication failed!")
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
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed successfully.")
            return redirect("teacher_dashboard")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "teachers/password_reset.html", {"form": form})


# ✅ Teacher Dashboard
from django.db.models import Prefetch, Avg

@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    teacher = request.user.teacher
    assigned_subjects = teacher.assigned_subjects.all()

    # ✅ Get all students, regardless of whether they have results
    students = Student.objects.all()  

    # ✅ Fetch results for assigned subjects
    results = Result.objects.filter(course__in=assigned_subjects).select_related("student", "course")

    # ✅ Dictionary to store student results
    student_results = {}
    for result in results:
        if result.student.id not in student_results:
            student_results[result.student.id] = {}
        student_results[result.student.id][result.course.id] = result.grade

    # ✅ Calculate average for teacher's assigned subjects
    assigned_avgs = []
    for subject in assigned_subjects:
        subject_results = Result.objects.filter(course=subject)
        if subject_results.exists():
            avg_score = subject_results.aggregate(avg=Avg('marks'))['avg']
            assigned_avgs.append(avg_score)
    assigned_subject_avg = round(sum(assigned_avgs) / len(assigned_avgs), 2) if assigned_avgs else "N/A"

    # ✅ Calculate overall analytics for ALL courses
    all_courses = Course.objects.all()
    all_subjects = []
    all_averages = []
    for course in all_courses:
        course_results = Result.objects.filter(course=course)
        if course_results.exists():
            avg_course = course_results.aggregate(avg=Avg('marks'))['avg']
            all_subjects.append(course.name)
            all_averages.append(avg_course)

    context = {
        "teacher": teacher,
        "assigned_subjects": assigned_subjects,
        "students": students,  # ✅ Now includes all students
        "student_results": student_results,  # ✅ Ensures we can access results in the template
        "assigned_subject_avg": assigned_subject_avg,
        "all_subjects": all_subjects,  # ✅ For graph
        "all_averages": all_averages,  # ✅ For graph
    }
    return render(request, "teachers/dashboard.html", context)
# ✅ Teachers Can View All Results
@login_required
@user_passes_test(is_teacher)

def teacher_results(request):
    students = Student.objects.all()
    subjects = Course.objects.all()  # ✅ Ensure subjects are retrieved

    student_data = []
    for student in students:
        row = {
            "student": student,
            "grades": [],
        }
        for subject in subjects:
            result = Result.objects.filter(student=student, course=subject).first()
            row["grades"].append(result.grade if result else "-")  # Show "-" if no result
        
        student_data.append(row)

    context = {
        "students": student_data,
        "subjects": subjects,  # ✅ Ensure subjects are included in context
    }
    return render(request, "teachers/results.html", context)

# ✅ Teacher Profile & Assign Subjects
@login_required
@user_passes_test(is_teacher)
def teacher_profile(request):
    teacher = request.user.teacher
    all_courses = Course.objects.all()

    if request.method == "POST":
        selected_courses = request.POST.getlist("assigned_subjects")
        teacher.assigned_subjects.set(selected_courses)
        teacher.save()
        messages.success(request, "Subjects updated successfully.")
        return redirect("teacher_profile")

    return render(request, "teachers/profile.html", {
        "teacher": teacher,
        "all_courses": all_courses
    })


# ✅ Teachers Can Add & Edit Student Results (General Version)
@login_required
@user_passes_test(is_teacher)
@login_required
@user_passes_test(is_teacher)
def teacher_results(request):
    # ✅ Fetch all results for all students
    results = Result.objects.all()

    return render(request, "teachers/results.html", {
        "results": results,
    })


# ✅ View Students Assigned to a Teacher (Renamed to teacher_students)
@login_required
@user_passes_test(is_teacher)
def teacher_students(request):
    teacher = request.user.teacher
    # Query students having at least one result in teacher's assigned subjects
    students = Student.objects.filter(result__course__in=teacher.assigned_subjects.all()).distinct()
    return render(request, "teachers/view_students.html", {"students": students})


@login_required
@user_passes_test(is_teacher)
def teacher_add_student_results(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    try:
        teacher = request.user.teacher
        assigned_subjects = teacher.assigned_subjects.all()  # ✅ Get assigned subjects
    except Teacher.DoesNotExist:
        messages.error(request, "You are not assigned any subjects.")
        return redirect("teacher_dashboard")

    selected_course_id = None
    existing_result = None

    if request.method == "POST":
        course_id = request.POST.get("course_id")
        marks = request.POST.get("marks")

        # ✅ Allow teacher to add results for any subject, not just assigned ones
        course = get_object_or_404(Course, id=course_id)

        # ✅ Update if exists, create if new
        result, created = Result.objects.update_or_create(
            student=student,
            course=course,
            defaults={"marks": marks}
        )

        # ✅ Use session to prevent messages appearing on login
        if created:
            request.session["success_message"] = "New result added successfully!"
        else:
            request.session["success_message"] = "Result updated successfully!"

        return redirect("teacher_dashboard")

    # ✅ Check for existing result
    elif request.GET.get("course_id"):
        selected_course_id = request.GET.get("course_id")
        existing_result = Result.objects.filter(student=student, course_id=selected_course_id).first()

    # ✅ Retrieve success message from session
    success_message = request.session.pop("success_message", None)

    context = {
        "student": student,
        "assigned_subjects": assigned_subjects,
        "selected_course_id": selected_course_id,
        "existing_result": existing_result,
        "success_message": success_message,  # ✅ Pass to template
    }
    return render(request, "teachers/add_results.html", context)

# ✅ Teachers Can Edit Results
@login_required
@user_passes_test(is_teacher)
def teacher_edit_result(request, result_id):
    result = get_object_or_404(Result, id=result_id)

    if result.course not in request.user.teacher.assigned_subjects.all():
        messages.error(request, "You are not allowed to edit this result.")
        return redirect("teacher_manage_results")

    if request.method == "POST":
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect("teacher_manage_results")
    else:
        form = ResultForm(instance=result)

    return render(request, "teachers/edit_result.html", {
        "form": form,
        "result": result
    })


# ✅ View List of Teachers
@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teacher_list.html", {"teachers": teachers})


# ✅ Manage Results (Add & Edit)
@login_required
@user_passes_test(is_teacher)
def teacher_manage_results(request):
    teacher = request.user.teacher
    assigned_subjects = teacher.assigned_subjects.all()
    results = Result.objects.filter(course__in=assigned_subjects)

    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Result added successfully!")
            return redirect("teacher_manage_results")
    else:
        form = ResultForm()

    return render(request, "teachers/manage_results.html", {
        "results": results,
        "form": form
    })
