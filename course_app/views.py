from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'course_app/courses_list.html', context={"courses": courses}) 


def courses(request):
    return render(request, 'course_app/courses.html')