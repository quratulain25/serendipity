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
        page = kwargs.pop('page', '')
        super(TaskForm, self).__init__(*args, **kwargs)
        if page:
            self.fields['page'].empty_label = None
            self.fields['page'].queryset = Page.objects.filter(id=page)
