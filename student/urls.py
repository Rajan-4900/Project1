from django.urls import path
from student.views import index, student , view_student , update_student


urlpatterns = [
    path("main/", index, name='index'),
    path("main/index.html", index, name='index'),
    path("main/student.html", student, name='student'),
    path('main/view_student.html', view_student, name="view_student"),
    path('main/update.student.html<int:id>', update_student, name="update_student")
]