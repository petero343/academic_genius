from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
def custom_admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Only allow staff/admin users
            login(request, user)
            return redirect("/admin/")  # Redirect to the admin dashboard
        else:
            messages.error(request, "Invalid credentials or insufficient permissions")

    return render(request, "users/admin_login.html")  # Load the custom login template
