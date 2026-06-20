import random
from io import BytesIO

from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image, ImageDraw, ImageFont

from constants import (
    ABOUT_MAX_LENGTH,
    AVATAR_COLORS,
    AVATAR_FONT_SIZE,
    AVATAR_SIZE,
    AVATAR_TEXT_COLOR,
    NAME_MAX_LENGTH,
    PHONE_MAX_LENGTH,
)
from validators import validate_github_url

from .managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name='Имя')
    surname = models.CharField(max_length=NAME_MAX_LENGTH, verbose_name='Фамилия')
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватарка'
    )
    phone = models.CharField(max_length=PHONE_MAX_LENGTH, verbose_name='Номер телефона')
    github_url = models.URLField(
        blank=True,
        validators=[validate_github_url],
        verbose_name='Ссылка на GitHub'
    )
    about = models.TextField(
        max_length=ABOUT_MAX_LENGTH,
        blank=True,
        verbose_name='Описание профиля'
    )

    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
    is_staff = models.BooleanField(default=False, verbose_name='Администратор')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_short_name(self):
        return self.name

    def _generate_avatar(self):
        """Генерирует аватарку с первой буквой имени на цветном фоне."""
        bg_color = random.choice(AVATAR_COLORS)

        image = Image.new('RGB', AVATAR_SIZE, bg_color)
        draw = ImageDraw.Draw(image)

        first_letter = self.name[0].upper() if self.name else '?'

        try:
            # Windows
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", AVATAR_FONT_SIZE)
        except:
            try:
                # Linux
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", AVATAR_FONT_SIZE)
            except:
                # macOS
                try:
                    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", AVATAR_FONT_SIZE)
                except:
                    font = ImageFont.load_default()

        draw.text(
            (AVATAR_SIZE[0] // 2, AVATAR_SIZE[1] // 2),
            first_letter,
            fill=AVATAR_TEXT_COLOR,
            font=font,
            anchor='mm'
        )

        buffer = BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)

        return ContentFile(buffer.read(), f'avatar_{self.email}.png')

    def save(self, *args, **kwargs):
        if not self.avatar:
            self.avatar = self._generate_avatar()
        super().save(*args, **kwargs)


class FavoriteProject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'project'],
                name='unique_user_project_favorite'
            )
        ]
        verbose_name = 'Избранный проект'
        verbose_name_plural = 'Избранные проекты'

    def __str__(self):
        return f"{self.user.email} - {self.project.name}"