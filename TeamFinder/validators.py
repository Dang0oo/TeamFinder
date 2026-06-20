# teamfinder/validators.py
from django.core.exceptions import ValidationError


def validate_github_url(value):
    """Проверяет, что ссылка ведёт на GitHub"""
    if value and 'github.com' not in value:
        raise ValidationError('Ссылка должна вести на GitHub (github.com)')