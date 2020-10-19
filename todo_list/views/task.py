from django.shortcuts import render, redirect, get_object_or_404

from todo_list.forms import TaskForm
from todo_list.models import Task


def create_task_view(request, page_id=0):
    if request.method == 'GET':
        form = TaskForm(page=page_id)
        return render(request, 'todo_list/task/task_create.html', {'form': form})

    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')
        return render(request, 'todo_list/task/task_create.html', {'form': form})


def edit_task_view(request, pk=0):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'todo_list/task/task_create.html', {'form': form})

    else:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')

        return render(request, 'todo_list/task/task_create.html', {'form': form})


def delete_task_view(request, pk=0):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo_list:list_page')
