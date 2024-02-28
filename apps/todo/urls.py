from django.urls import path
from apps.todo.views import (
    get_all_tasks,
    create_new_task
)

app_name = "tasks"

urlpatterns = [
    path("", get_all_tasks, name='all-tasks'),
    path("create/", create_new_task, name='create-task')
]