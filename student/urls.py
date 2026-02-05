from django.urls import path
from student.views import index, student


urlpatterns = [
    path("main/", index, name='index'),
    path("main/index.html", index, name='index'),
    path("main/student.html", student, name='student'),
]