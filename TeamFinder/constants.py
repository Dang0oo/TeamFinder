# Статусы проектов
PROJECT_STATUS_OPEN = 'open'
PROJECT_STATUS_CLOSED = 'closed'

PROJECT_STATUS_CHOICES = [
    (PROJECT_STATUS_OPEN, 'Открыт'),
    (PROJECT_STATUS_CLOSED, 'Закрыт'),
]

PROJECT_STATUS_MAX_LENGTH = 6

# Максимальная длина названия проекта
PROJECT_NAME_MAX_LENGTH = 200

# Настройки пагинации
USERS_PAGINATE_BY = 12
PROJECTS_PAGINATE_BY = 12
ADMIN_LIST_PER_PAGE = 20

# Настройки аватарок
AVATAR_SIZE = (200, 200)           # Размер аватарки (ширина, высота)
AVATAR_FONT_SIZE = 120             # Размер шрифта на аватарке
AVATAR_TEXT_COLOR = (255, 255, 255) # Цвет текста на аватарке (белый)

# Цвета для генерации аватарок (спокойные оттенки)
AVATAR_COLORS = [
    (70, 130, 180),
    (100, 149, 237),
    (72, 61, 139),
    (60, 179, 113),
    (210, 105, 30),
    (147, 112, 219),
    (52, 73, 94),
    (41, 128, 185),
    (39, 174, 96),
    (155, 89, 182),
    (52, 152, 219),
    (46, 204, 113),
]

# Максимальная длина полей пользователя
PHONE_MAX_LENGTH = 12
NAME_MAX_LENGTH = 124
ABOUT_MAX_LENGTH = 256