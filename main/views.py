from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateTopicForm, AddEntryForm


def index(request):
    return HttpResponse('Hello world')


def create_topic(request):
    if request.method == "post":
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            form.save()


def add_entry(request):
    if request.method == "post":
        form = AddEntryForm(request.POST)
        if form.is_valid():
            form.save()
