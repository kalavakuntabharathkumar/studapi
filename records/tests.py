import pytest
from rest_framework.test import APIClient
from .models import Student
@pytest.mark.django_db
def test_create_and_list_student():
    client=APIClient()
    payload={"student_number":"ST-100","first_name":"Asha","last_name":"Rao",
             "email":"asha@example.com","grade":"A","active":True}
    response=client.post("/api/students/",payload,format="json")
    assert response.status_code==201
    listing=client.get("/api/students/")
    assert listing.status_code==200
    assert listing.data["count"]==1
@pytest.mark.django_db
def test_grade_filter_and_report():
    Student.objects.create(student_number="ST-1",first_name="A",last_name="One",email="a@example.com",grade="A")
    Student.objects.create(student_number="ST-2",first_name="B",last_name="Two",email="b@example.com",grade="B")
    assert APIClient().get("/api/students/?grade=A").data["count"]==1
    report=APIClient().get("/api/reports/summary/")
    assert report.status_code==200
    assert report.data["total_students"]==2
@pytest.mark.django_db
def test_duplicate_student_number_rejected():
    Student.objects.create(student_number="ST-1",first_name="A",last_name="One",email="a@example.com")
    response=APIClient().post("/api/students/",{"student_number":"ST-1","first_name":"B","last_name":"Two","email":"b@example.com"},format="json")
    assert response.status_code==400

@pytest.mark.django_db
def test_health_endpoint():
    response=APIClient().get('/api/health/')
    assert response.status_code==200
    assert response.data['status']=='ok'
