from django.http.response import JsonResponse
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from task_app import serializers
from task_app.serializers import TaskSerializer,TeamSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated  
from .models import Task, Team
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token




def root(request):
    response = JsonResponse({'status':True,'message':'success'}, status=500)
    return response


         

# class TaskList(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class UpdateTask(generics.RetrieveUpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class CreateTask(generics.CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class CreateTeam(generics.CreateAPIView):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer




# class UserAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })















@api_view(['GET','POST'])
def taskList(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many = True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

@api_view(['GET','PUT'])
def taskDetails(request,id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task) 
        return Response(serializer.data)   
    

    if request.method == 'PUT':

        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(status=status.HTTP_404_NOT_FOUND) 
       


@api_view(['GET','POST'])
def teamList(request):
    if request.method == "GET":
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many = True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    