from django.shortcuts import render
from .models import Employee
from rest_framework import serializers,request,generics,viewsets
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
