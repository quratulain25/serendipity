from django.shortcuts import render, redirect

from todo_list.forms import PageForm, TaskForm
from todo_list.models import Page, Task


def dashboard_view(request):
    return render(request, 'dashboard.html')


# Page Views #

def list_page_view(request):
    page_list = Page.objects.all()
    task_list = Task.objects.all()

    context = {'page_list': page_list, 'task_list': task_list}
    return render(request, 'todo_list/page/page_list.html', context)


def create_page_view(request):
    if request.method == 'GET':
        form = PageForm()
        return render(request, 'todo_list/page/page_create.html', {'form': form})

    else:
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')


def edit_page_view(request, pk=0):
    page = Page.objects.get(pk=pk)

    if request.method == 'GET':
        form = PageForm(instance=page)
        return render(request, 'todo_list/page/page_create.html', {'form': form})

    else:
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')


def delete_page_view(request, pk=0):
    page = Page.objects.get(pk=pk)
    page.delete()
    return redirect('todo_list:list_page')


# Task Views #

def create_task_view(request, page_id=0):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'todo_list/task/task_create.html', {'form': form})

    else:
        data = request.POST.copy()
        data['page'] = page_id  # set FK

        form = TaskForm(data)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')


def edit_task_view(request, pk=0):
    task = Task.objects.get(pk=pk)

    if request.method == 'GET':
        form = TaskForm(instance=task)
        form.id = task.id
        return render(request, 'todo_list/task/task_create.html', {'form': form})

    else:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')


def delete_task_view(request, pk=0):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('todo_list:list_page')
