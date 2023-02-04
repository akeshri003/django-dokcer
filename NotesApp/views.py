from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from NotesApp.serializers import NoteSerializer, UserSerializer
from NotesApp.models import Note
from django.contrib.auth.models import User
from rest_framework import permissions
from NotesApp.permissions import IsOwnerOrReadOnly
from rest_framework import generics


# Create your views here.

class NoteView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer










# class NoteView(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     def get(self, request, format=None):
#         note = Note.objects.all()
#         serializer = NoteSerializer(note, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class NoteDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     def get_object(self, pk):
#         try:
#             return Note.objects.get(pk=pk)
#         except Note.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


# class UserList(APIView):

#     def get(self, request, format=None):
#         users = User.objects.all()
#         user_serializer = UserSerializer(users)
#         return Response(user_serializer.data)

#     def post(self, request, format=None):
#         user_serializer = UserSerializer(data=request.data, many=True)
#         if user_serializer.is_valid:
#             user_serializer.save()
#             return Response(user_serializer.data)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetail(APIView):

#     def get_user_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)
        
#     def get(self, request, pk, format=None):
#         users = self.get_user_object(pk)
#         user_serializer = UserSerializer(users)
#         return Response(user_serializer.data)

#     def put(self, request, pk, format=None):
#         users = self.get_user_object(pk)
#         user_serializer = UserSerializer(users, data = request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response(user_serializer, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         users = self.get_user_object(pk)
#         users.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)

    