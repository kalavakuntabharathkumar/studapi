from django.db.models import Count
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Staff
from .serializers import StudentSerializer, StaffSerializer
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def get_queryset(self):
        qs=super().get_queryset()
        grade=self.request.query_params.get("grade")
        active=self.request.query_params.get("active")
        if grade: qs=qs.filter(grade=grade)
        if active in ("true","false"): qs=qs.filter(active=(active=="true"))
        return qs
class StaffViewSet(viewsets.ModelViewSet):
    serializer_class=StaffSerializer
    queryset=Staff.objects.all()
@api_view(["GET"])
def report_summary(request):
    rows=Student.objects.values("grade").annotate(student_count=Count("id")).order_by("grade")
    return Response({"total_students":Student.objects.count(),"by_grade":list(rows)})
def health(request): return JsonResponse({"status":"ok","service":"student-records-api"})
