from django.contrib import admin
from .models import User, FavoriteProject

admin.site.register(User)
admin.site.register(FavoriteProject)