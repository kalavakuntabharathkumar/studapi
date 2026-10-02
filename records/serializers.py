from rest_framework import serializers
from .models import Student, Staff
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["id","student_number","first_name","last_name","email","grade","active","created_at"]
        read_only_fields=["id","created_at"]
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields=["id","employee_number","name","email","department"]
