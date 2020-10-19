from django.shortcuts import render, redirect, get_object_or_404

from todo_list.forms import PageForm
from todo_list.models import Page, Task


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

        return render(request, 'todo_list/page/page_create.html', {'form': form})


def edit_page_view(request, pk=0):
    page = get_object_or_404(Page, pk=pk)

    if request.method == 'GET':
        form = PageForm(instance=page)
        return render(request, 'todo_list/page/page_create.html', {'form': form})

    else:
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('todo_list:list_page')

        return render(request, 'todo_list/page/page_create.html', {'form': form})


def delete_page_view(request, pk=0):
    page = get_object_or_404(Page, pk=pk)
    page.delete()
    return redirect('todo_list:list_page')
