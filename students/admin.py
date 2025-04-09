from django.contrib import admin
from .models import Student

# Unregister first if already registered
if admin.site.is_registered(Student):
    admin.site.unregister(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("adm_number", "first_name", "last_name", "dob", "age")  # Now 'age' works
    search_fields = ("adm_number", "first_name", "last_name")
    list_filter = ("dob",)
    
    fields = ("adm_number", "first_name", "last_name", "dob")  # No 'age' here since it's calculated
    readonly_fields = ("adm_number",)  # No 'age' here either

    def age(self, obj):
        """Display age in the list view"""
        return obj.age()

    age.admin_order_field = "dob"  # Allow sorting by age
    age.short_description = "Age"
