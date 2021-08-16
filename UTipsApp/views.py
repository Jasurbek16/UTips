from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from .models import Subjects, Info
from .forms import (
    AddSubjectsForm,
    AddTopicsForm
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    subjects = Subjects.objects.order_by('name').all()
    pages = Paginator(subjects, 4)
    page = request.GET.get('page')
    subject_page = pages.get_page(page)

    if request.user.is_authenticated:
        topics = Info.objects.filter(author=request.user).order_by('-date_shared').all()
    else:    
        topics = Info.objects.order_by('-date_shared').all()
    context = {
        'subjects':subjects,
        'subject_page':subject_page,
        'topics':topics
    }
    return render(request, 'UTipsApp/home.html', context)

def UserTopics(request, name):
    user = get_object_or_404(User, username=name)
    topics = Info.objects.filter(author=user).order_by('-date_shared')
    pages = Paginator(topics, 3)
    page = request.GET.get('page')
    topic_page = pages.get_page(page)

    context = {
        'topic_page':topic_page,
        'topics':topics,
    }
    return render(request, 'UTipsApp/user_topics.html', context)

def about(request):
    subjects = Subjects.objects.order_by('name').all()
    if request.user.is_authenticated:
        topics = Info.objects.filter(author=request.user).order_by('-date_shared').all()
    else:    
        topics = Info.objects.order_by('-date_shared').all()
    context = {
        'subjects':subjects,
        'topics':topics
    }
    return render(request, "UTipsApp/about.html", context)


def subject_details(request, pk):
    # For the single subject
    subject = Subjects.objects.get(id=pk)
    topics = subject.info_set.order_by("-date_shared")
    pages = Paginator(topics, 4)
    page = request.GET.get('page')
    topic_page = pages.get_page(page)
    context = {
        "subject": subject, 
        "topics": topics,
        "topic_page": topic_page,
    }
    return render(request, "UTipsApp/topic_list.html", context)



def topic_details(request, pk):
    # For the single topic
    topic = Info.objects.get(id=pk)
    subject = Subjects.objects.get(id=topic.subject.id)
    context = {"topic": topic, "subject": subject}
    return render(request, "UTipsApp/topic.html", context)

@login_required
def addSubject(request):
    if request.method != "POST":
        form = AddSubjectsForm()
    else:
        form = AddSubjectsForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, f"The {name} has been added successfully 👏")
            return redirect("Ut-home")

    context = {"form": form}
    return render(request, "UTipsApp/add_subject.html", context)


@login_required
def addTopic(request, pk):
    subject = Subjects.objects.get(id = pk)
    if request.method != "POST":
        form = AddTopicsForm()
    else:
        form = AddTopicsForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.subject = subject
            form.save()
            topic = form.cleaned_data.get("topic")
            messages.success(request, f"The {topic} has been added successfully 👏")
            return redirect("Ut-home")

    context = {"form": form}
    return render(request, "UTipsApp/add_topic.html", context)


class TopicEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Info
    fields = ['topic', 'text', 'date_shared']
    template_name = 'UTipsApp/edit_topic.html'
    
    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.author:
            return True
        return False


class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Info
    success_url = '/'

    def test_func(self):
       topic = self.get_object()
       if self.request.user == topic.author:
           return True
       return False

    