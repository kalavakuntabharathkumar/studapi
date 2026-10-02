from django.contrib import admin
from django.urls import path, include
from records.views import health
urlpatterns=[path("admin/",admin.site.urls),path("api/",include("records.urls")),path("api/health/",health)]
