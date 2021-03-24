from django.shortcuts import render
from django.shortcuts import render



from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from rest_framework import generics,mixins
from rest_framework import viewsets
from view_sets_app.models import Student
from view_sets_app.serializers import StudentSerializer


# Create your views here.

#using ModelViewSet we can edit delete data and view data
class StudentViewSet(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

#Uisng read only we can just read the data !
class StudentViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer


   #both primary key based and non primary key based operation are be done by this class !
   #dont need to define any other class  for the primary key operation !
   #it will handle  primary key autometically !

