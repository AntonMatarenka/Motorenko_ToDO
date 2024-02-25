from django.contrib import admin

from apps.todo.models import (
    Task,
    SubTask,
    Status,
    Category,
    Priority

)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_by', 'created_at', )
    list_filter = ('category', 'status', 'created_by', 'created_at', )

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'task', 'status', 'created_by', 'created_at',)
    list_filter = ('task', 'category', 'status', 'created_by', 'created_at',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_filter = ('name', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name', )

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_filter = ('name', )