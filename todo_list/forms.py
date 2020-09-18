from django import forms

from todo_list.models import Page, Task


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['is_complete'].required = False
