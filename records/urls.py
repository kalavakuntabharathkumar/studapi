from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, StaffViewSet, report_summary
router=DefaultRouter()
router.register("students",StudentViewSet,basename="student")
router.register("staff",StaffViewSet,basename="staff")
urlpatterns=[path("",include(router.urls)),path("reports/summary/",report_summary)]
