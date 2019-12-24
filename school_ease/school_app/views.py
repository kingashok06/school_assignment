from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor,School ,Coaching
from django.http import JsonResponse
from .serializers import TutorSerializer,SchoolSerializer,CoachingSerializer
from rest_framework import generics
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

from rest_framework import viewsets


def user_login(request):
    context = {}
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user success'))

        else:
            context["error"]: "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

def success(request):
    context = {}
    context['user'] = request.user
    return render(request , 'auth/success.html', context)

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("user_login "))


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CoachingViewSet(viewsets.ModelViewSet):
    queryset = Coaching.objects.all()
    serializer_class = CoachingSerializer


def home(request):
    api_data = {
        "Tutor Urls":{
            "List of Tutors [GET Request]": "http://localhost:8000/tutors/",
            "Add Tutor [POST Request]": "http://localhost:8000/tutors/",
            "Get Perticular Tutor [GET Request]": "http://localhost:8000/tutors/<id>",
            "Update Tutor [PUT Request]": "http://localhost:8000/tutors/<id>",
            "Delete Tutor [DELETE Request]": "http://localhost:8000/tutors/<id>"
        },
        "School Urls": {
            "List of Schools [GET Request]": "http://localhost:8000/schools/",
            "Add School [POST Request]": "http://localhost:8000/schools/",
            "Get Perticular School [GET Request]": "http://localhost:8000/schools/<id>",
            "Update School [PUT Request]": "http://localhost:8000/schools/<id>",
            "Delete School [DELETE Request]": "http://localhost:8000/schools/<id>"
        },
        "Coaching Urls": {
            "List of Coachings [GET Request]": "http://localhost:8000/coaching/",
            "Add Coaching [POST Request]": "http://localhost:8000/coaching/",
            "Get Perticular Coaching [GET Request]": "http://localhost:8000/coaching/<id>",
            "Update Coaching [PUT Request]": "http://localhost:8000/coaching/<id>",
            "Delete Coaching [DELETE Request]": "http://localhost:8000/coaching/<id>"
        }
    }
    return JsonResponse(api_data)
