from django.contrib import admin
from django.urls import path
from students.views import home, student_list, student_detail, student_add, student_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('students/add/', student_add, name='student_add'),
    path('students/<int:id>/', student_detail, name='student_detail'),
    path('students/<int:id>/delete/', student_delete, name='student_delete'),
]
