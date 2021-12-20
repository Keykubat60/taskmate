from todolist_app.models import TaskList
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ["task", "done"]
