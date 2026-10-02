from django.contrib import admin
from .models import Student, Staff
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("student_number","first_name","last_name","grade","active")
    search_fields=("student_number","first_name","last_name","email")
    list_filter=("grade","active")
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display=("employee_number","name","department")
    search_fields=("employee_number","name","email")
    list_filter=("department",)
