from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from employee.serializers import EmployeeSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
