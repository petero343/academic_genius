from django.contrib import admin
from .models import Teacher  # ✅ Only import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_number', 'email', 'date_joined')
    search_fields = ("first_name", "last_name", "id_number", "email")
    list_filter = ("date_joined",)
    ordering = ("date_joined",)

admin.site.register(Teacher, TeacherAdmin)  # ✅ Register the Teacher model
