from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from poll.models import Question
from poll.serailizers import QuestionSerializer


# Create your views here.
class PollListView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class PollAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PollDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response({'error': 'Given question object not found.'}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        return Response({'success': 'Poll deleted successfully!'}, status=204)


@csrf_exempt
def poll(request):
    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def poll_details(request, id):
    try:
        instance = Question.objects.get(id=id)
    except Question.DoesNotExist as e:
        return JsonResponse({'error': 'Given question object not found.'}, status=404)
    if request.method == "GET":
        serializer = QuestionSerializer(instance)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        instance.delete()
        return JsonResponse({'success': 'Poll deleted successfully!'}, status=400)
