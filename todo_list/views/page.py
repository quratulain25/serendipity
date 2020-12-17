from django.shortcuts import render


def list_page_view(request):
    return render(request, 'todo_list/page/page_list.html')


def create_page_view(request, pk=0):
    return render(request, 'todo_list/page/page_create.html')
