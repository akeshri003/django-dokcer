from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from NotesApp import views

urlpatterns = [
    path('notes/', views.NoteView.as_view()),
    path('notes/<int:pk>', views.NoteDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
