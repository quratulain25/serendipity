from django.shortcuts import render


def create_task_view(request, page_id=0, pk=0):
    return render(
        request, 'todo_list/task/task_create.html', {'page': page_id, 'pk': pk}
    )
