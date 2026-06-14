from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Project(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Открыт'),
        ('CLOSED', 'Закрыт'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
