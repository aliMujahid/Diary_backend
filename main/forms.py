from django import forms

from .models import Topic, Entry


class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name",]


class AddEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text",]
