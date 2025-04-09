from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import get_template
from users.models import CustomUser
from students.models import Student, Course
from teachers.models import Teacher

# =================================================================================
# ✅ Custom Admin Access Restriction
# =================================================================================
def admin_required(user):
    """ Restrict access to admin-only views """
    return user.is_authenticated and user.is_staff

# =================================================================================
# ✅ Admin Authentication Views
# =================================================================================
def admin_login(request):
    """ Custom Admin Login """
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("custom_admin_dashboard")  # Redirect if already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user and user.is_staff:
            login(request, user)
            return redirect("custom_admin_dashboard")
        else:
            messages.error(request, "Invalid credentials or insufficient permissions.")

    return render(request, "users/admin_login.html")


@login_required
@user_passes_test(admin_required)
def admin_logout(request):
    """ Admin Logout """
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("custom_admin_login")


@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    """ Admin Dashboard Home """
    context = {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
        "total_courses": Course.objects.count(),
    }
    return render(request, "users/admin_dashboard.html", context)


# =================================================================================
# ✅ Teachers Management
# =================================================================================
@login_required
@user_passes_test(admin_required)
def manage_teachers(request):
    """ View all teachers """
    teachers = Teacher.objects.all()
    return render(request, "users/teachers.html", {"teachers": teachers})


@login_required
@user_passes_test(admin_required)
def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        id_number = request.POST["id_number"]
        email = request.POST["email"]
        date_joined = request.POST["date_joined"]
        selected_courses = request.POST.getlist("assigned_subjects")  # Get multiple selected subjects
        
        # Create teacher object (without subjects first)
        teacher = Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            id_number=id_number,
            email=email,
            date_joined=date_joined
        )
        
        # ✅ Correct way to assign ManyToManyField
        teacher.assigned_subjects.set(selected_courses)  
        
        messages.success(request, "Teacher added successfully!")
        return redirect("manage_teachers")

    courses = Course.objects.all()  # Fetch courses for selection
    return render(request, "users/admin_add_teacher.html", {"courses": courses})


@login_required
@user_passes_test(admin_required)
def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":
        teacher.first_name = request.POST["first_name"]
        teacher.last_name = request.POST["last_name"]
        
        # Fixing ManyToManyField Assignment
        assigned_subjects_ids = request.POST.getlist("assigned_subjects")  # Get list of selected course IDs
        assigned_subjects = Course.objects.filter(id__in=assigned_subjects_ids)  # Query courses
        
        # Assign subjects correctly
        teacher.assigned_subjects.set(assigned_subjects)  

        teacher.save()
        messages.success(request, "Teacher details updated successfully!")
        return redirect("manage_teachers")  

    courses = Course.objects.all()  # Get all courses for selection
    return render(request, "users/edit_teacher.html", {"teacher": teacher, "courses": courses})


@login_required
@user_passes_test(admin_required)
def delete_teacher(request, teacher_id):
    """ Delete a teacher """
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == "POST":  # Ensure it's a POST request
        teacher.delete()
        messages.success(request, "Teacher deleted successfully.")
        return redirect("manage_teachers")

    return render(request, "users/delete_teacher.html", {"teacher": teacher})


# =================================================================================
# ✅ Students Management
# =================================================================================
@login_required
@user_passes_test(admin_required)
def manage_students(request):
    """ View all students """
    try:
        template = get_template("users/students.html")  # Check if template exists
        students = Student.objects.exclude(id=None)  # Ensures only valid students are retrieved
        return render(request, "users/students.html", {"students": students})
    except Exception as e:
        return HttpResponse(f"Template Error: {e}")  # Show error in the browser


@login_required
@user_passes_test(admin_required)

def add_student(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dob = request.POST.get("dob")

        # 🔹 Generate the admission number
        last_student = Student.objects.order_by("-id").first()
        if last_student:
            last_adm_number = int(last_student.adm_number.replace("STU", ""))
            adm_number = f"STU{last_adm_number + 1}"
        else:
            adm_number = "STU1001"

        # 🔹 Save student
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            adm_number=adm_number,  # Auto-generated
        )
        return redirect("manage_students")  # Redirect to student list

    return render(request, "users/add_student.html")

@login_required
@user_passes_test(admin_required)
def edit_student(request, student_id):
    """ Edit student details """
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.first_name = request.POST["first_name"]
        student.last_name = request.POST["last_name"]
        student.adm_number = request.POST["adm_number"]
        student.dob = request.POST["dob"]
        student.save()
        messages.success(request, "Student details updated successfully.")
        return redirect("manage_students")

    return render(request, "users/edit_student.html", {"student": student})


@login_required
@user_passes_test(admin_required)
def delete_student(request, student_id):
    """ Delete a student """
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":  # Ensure it's a POST request
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("manage_students")

    return render(request, "users/delete_student.html", {"student": student})


# =================================================================================
# ✅ Courses Management
# =================================================================================
@login_required
@user_passes_test(admin_required)
def manage_courses(request):
    courses = Course.objects.all().exclude(id=None)  # Ensures only valid courses are retrieved
    return render(request, "users/courses.html", {"courses": courses})


@login_required
@user_passes_test(admin_required)
def add_course(request):
    """ Add a new course """
    if request.method == "POST":
        course = Course.objects.create(
            name=request.POST["name"],
            code=request.POST["code"],
        )
        messages.success(request, "Course added successfully.")
        return redirect("manage_courses")

    return render(request, "users/add_course.html")


@login_required
@user_passes_test(admin_required)
def edit_course(request, course_id):
    """ Edit course details """
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.name = request.POST["name"]
        course.code = request.POST["code"]
        course.save()
        messages.success(request, "Course details updated successfully.")
        return redirect("manage_courses")

    return render(request, "users/edit_course.html", {"course": course})


@login_required
@user_passes_test(admin_required)
def delete_course(request, course_id):
    """ Delete a course """
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":  # Ensure it's a POST request
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect("manage_courses")

    return render(request, "users/delete_course.html", {"course": course})


# Edit Student
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.first_name = request.POST["first_name"]
        student.last_name = request.POST["last_name"]
        student.adm_number = request.POST["adm_number"]
        student.dob = request.POST["dob"]
        student.save()
        messages.success(request, "Student updated successfully!")
        return redirect("manage_students")

    return render(request, "users/admin_edit_student.html", {"student": student})

# Delete Student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect("manage_students")

# ========================= COURSE VIEWS ========================= #


# Edit Course
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.name = request.POST["name"]
        course.code = request.POST["code"]
        course.save()
        messages.success(request, "Course updated successfully!")
        return redirect("manage_courses")

    return render(request, "users/admin_edit_course.html", {"course": course})

# Delete Course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, "Course deleted successfully!")
    return redirect("manage_courses")


from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from students.models import Student, Result

# ✅ Check if User is an Admin
def is_admin(user):
    return user.is_authenticated and user.is_staff

# ✅ Admin: Manage Students & View Their Results
from django.shortcuts import render
from students.models import Student, Course, Result

def manage_students(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    # Create a dictionary to store results
    student_results = {student.id: {} for student in students}

    # Fetch results and populate the dictionary
    results = Result.objects.all()
    for result in results:
        student_results[result.student.id][result.course.id] = result.grade  # Store grades

    context = {
        'students': students,
        'courses': courses,
        'student_results': student_results,  # Results dictionary
    }
    return render(request, 'users/students.html', context)

from django import template
register = template.Library()

@register.filter
def dict_key(dictionary, key):
    return dictionary.get(key, {})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.dob = request.POST['dob']
        student.save()
        return redirect('manage_students')

    return render(request, 'users/edit_student.html', {'student': student})

# Delete Student View
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect('manage_students')

    return render(request, 'users/delete_student.html', {'student': student})

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # ✅ Redirect based on user role
            if hasattr(user, "teacher"):
                return redirect("teacher_dashboard")
            elif hasattr(user, "student"):
                return redirect("student_dashboard")
            elif user.is_superuser:
                return redirect("admin_dashboard")
            else:
                return redirect("home")  # Default fallback

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "users/login.html")
