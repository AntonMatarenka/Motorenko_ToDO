from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.todo.forms import CreateTaskForm
from apps.todo.models import (
    Task,
    Category,
    Status,
    Priority
)


def home_page(request):
    return render(
        request=request,
        template_name='main.html',
    )


def get_all_tasks(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }

    return render(
        request=request,
        template_name='todo/all_tasks.html',
        context=context
    )


def create_new_task(request):
    users = User.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    priorities = Priority.objects.all()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task_data = form.cleaned_data
            Task.objects.create(**task_data)
            return redirect('router:tasks:all-tasks')

        context = {
            "form": form,
            "users": users,
            "categories":categories,
            "statuses": statuses,
            "priorities": priorities
        }

    else:
        form = CreateTaskForm()
        context = {
            "form": form,
            "users": users,
            "categories": categories,
            "statuses": statuses,
            "priorities": priorities
        }

    return render(
        request=request,
        template_name='todo/create_task.html',
        context=context
    )



