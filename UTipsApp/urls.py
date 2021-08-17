"""Defines URL patterns for UniTipsApp"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TopicEditView, TopicDeleteView
from . import views

urlpatterns = [
    # Home Page
    path("", views.home, name="Ut-home"),
    path("user/<str:name>", views.UserTopics, name="user-topics"),
    path("about/", views.about, name="Ut-about"),
    
    path("topics/<int:pk>/", views.topic_details, name="topic-details"),
    path("topics/<int:pk>/edit/", TopicEditView.as_view(), name="edit-topic"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="delete-topic"),
    
    path("subjects/<int:pk>/", views.subject_details, name="subject-details"),
    path("subjects/new/", views.addSubject, name="add-subject"),
    path("subjects/<int:pk>/topics/new/", views.addTopic, name="add-topic"),


]
