from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile
import random


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен для заполнения')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None  # удаляем поле username
    
    # Основные поля
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=124, verbose_name='Имя')
    surname = models.CharField(max_length=124, verbose_name='Фамилия')
    profile_picture = models.ImageField(upload_to='profile_pics/', verbose_name='Аватарка')
    mobile = models.CharField(max_length=12, verbose_name='Номер телефона')
    git_profile = models.URLField(blank=True, verbose_name='Ссылка на GitHub')
    about = models.TextField(max_length=256, blank=True, verbose_name='Описание профиля')
    
    # Статусы
    is_active = models.BooleanField(default=True, verbose_name='Активный пользователь')
    is_staff = models.BooleanField(default=False, verbose_name='Администратор')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'mobile']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_short_name(self):
        return self.name

    def _generate_avatar(self):
        colors = [
            (70, 130, 180), (100, 149, 237), (72, 61, 139),
            (60, 179, 113), (210, 105, 30), (147, 112, 219),
            (52, 73, 94), (41, 128, 185), (39, 174, 96),
            (155, 89, 182), (52, 152, 219), (46, 204, 113),
        ]
        bg_color = random.choice(colors)
        
        size = (200, 200)
        image = Image.new('RGB', size, bg_color)
        draw = ImageDraw.Draw(image)
        
        first_letter = self.name[0].upper() if self.name else '?'
        
        try:
            font_size = 120
            font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), first_letter, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2
        
        draw.text((x, y), first_letter, fill=(255, 255, 255), font=font)
        
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        buffer.seek(0)
        
        return ContentFile(buffer.read(), f'avatar_{self.email}.png')

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            self.profile_picture = self._generate_avatar()
        super().save(*args, **kwargs)


class FavoriteProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.email} - {self.project.name}"