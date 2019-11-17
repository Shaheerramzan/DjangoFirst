from django.http import HttpRequest, HttpResponse
import json
from django.shortcuts import render
from FirstApp.models import Students


# Create your views here.
def index(request):
    return HttpResponse("hello world")


def user_first_view(request):
    roll_no_lt = request.GET.get('roll_num')

    students = Students.objects.filter(roll_num__exact=roll_no_lt)
    student_info = list()
    for student in students:
        info = {
            'name': student.name,
            'roll_number': student.roll_num,
            'section': student.sec
        }
        student_info.append(info)
    return HttpResponse(student_info)


def create_user(request):
    data = request.POST
    data = json.loads(data.decode('utf-8'))
    user = Students.objects.create(name=data['name'], roll_num=data['roll_num'], sec=data['section'])
    return HttpResponse("user created successfully")


def show_all_users(request):
    user = Students.objects.all()
    return HttpResponse(user)


def update_user(request):
    pass
