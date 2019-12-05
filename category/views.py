from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, SubCategory
from rest_framework.response import Response
from .serializers import CategorySerializers, SubCategorySerializers
from rest_framework import status, authentication, permissions, parsers


# Create your views here.


class GetCategoryList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializers(categories, many=True)
            return Response({'categories': serializer.data, 'status': status.HTTP_200_OK})
        except Category.DoesNotExist as exceptions:
            raise exceptions.ValidationError(
                {'error': 'User object not found.', 'status': status.HTTP_404_NOT_FOUND})


class CreateCategory(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        json_parser = parsers.JSONParser()
        data = json_parser.parse(request)
        serializer = CategorySerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category added successfully', 'category': serializer.data,
                             'status': status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateSubCategory(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        json_parser = parsers.JSONParser()
        data = json_parser.parse(request)
        serializer = SubCategorySerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Sub category added successfully', 'category': serializer.data,
                             'status': status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
