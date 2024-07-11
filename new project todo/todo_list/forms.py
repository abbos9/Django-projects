# ваше_приложение/forms.py
from django import forms
from todo_list.models import TodoList

class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'content', 'created','due_date','category']
