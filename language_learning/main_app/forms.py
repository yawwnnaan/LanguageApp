from django import forms
from .models import Word, Test

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation']

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['question', 'correct_answer', 'incorrect_answer1', 'incorrect_answer2', 'incorrect_answer3']