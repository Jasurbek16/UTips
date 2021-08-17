from django import forms
from .models import Subjects, Info


class AddSubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ["name", "professor"]
        label = {"subject": "", "professor": ""}


class AddTopicsForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ["topic", "text", "date_shared"]
        label = {
            "topic": "",
            "text": "",
            "date_shared": "",
        }
