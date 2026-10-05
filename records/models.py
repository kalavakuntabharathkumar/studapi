from django.db import models
class Student(models.Model):
    student_number=models.CharField(max_length=24,unique=True)
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    email=models.EmailField(unique=True)
    grade=models.CharField(max_length=12,default="N/A",db_index=True)
    active=models.BooleanField(default=True,db_index=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["last_name","first_name"]
        indexes=[models.Index(fields=["active","grade"],name="student_active_grade")]
    def __str__(self): return f"{self.student_number}: {self.first_name} {self.last_name}"
class Staff(models.Model):
    employee_number=models.CharField(max_length=24,unique=True)
    name=models.CharField(max_length=160)
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=80,db_index=True)
    def __str__(self): return self.name

# Composite index supports common active-student-by-grade filters.
