from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(
        max_length=1500,
        verbose_name='category details'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name[:15]}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Status(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name[:15]}"

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Priority(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name[:15]}"

    class Meta:
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'


class Task(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=75)
    description = models.TextField(
        max_length=1500,
        verbose_name='task details'
    )
    status = models.ForeignKey(
        Status,
        null=True,
        blank=True,
        on_delete=models.SET(1)
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    priority = models.ForeignKey(
        Priority,
        null=True,
        blank=True,
        on_delete=models.SET(1)
    )
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title[:25]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class SubTask(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=1500)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtasks'
    )
    status = models.ForeignKey(
        Status,
        null=True,
        blank=True,
        on_delete=models.SET(1)
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    priority = models.ForeignKey(
        Priority,
        null=True,
        blank=True,
        on_delete=models.SET(1)
    )
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title[:25]}..."

    class Meta:
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'

