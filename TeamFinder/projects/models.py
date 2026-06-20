from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from constants import (
    PROJECT_NAME_MAX_LENGTH,
    PROJECT_STATUS_CHOICES,
    PROJECT_STATUS_CLOSED,
    PROJECT_STATUS_MAX_LENGTH,
    PROJECT_STATUS_OPEN,
)
from validators import validate_github_url

User = get_user_model()


class Project(models.Model):
    STATUS_OPEN = PROJECT_STATUS_OPEN
    STATUS_CLOSED = PROJECT_STATUS_CLOSED
    STATUS_CHOICES = PROJECT_STATUS_CHOICES

    name = models.CharField(
        max_length=PROJECT_NAME_MAX_LENGTH,
        verbose_name='Название проекта'
    )
    description = models.TextField(blank=True, verbose_name='Описание проекта')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_projects',
        verbose_name='Автор проекта'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    github_url = models.URLField(
        blank=True,
        validators=[validate_github_url],
        verbose_name='Ссылка на GitHub'
    )
    status = models.CharField(
        max_length=PROJECT_STATUS_MAX_LENGTH,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
        verbose_name='Статус'
    )
    participants = models.ManyToManyField(
        User,
        related_name='participated_projects',
        blank=True,
        verbose_name='Участники проекта'
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})