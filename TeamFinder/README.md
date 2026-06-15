# TeamFinder
```md
**TeamFinder** — это веб-платформа для поиска команды и сотрудничества в IT-проектах. Сервис помогает разработчикам находить единомышленников, создавать совместные проекты и делиться идеями.

## Основные функции

- 👤 Регистрация и авторизация пользователей с подтверждением email
- 📝 Создание и управление проектами (название, описание, GitHub-ссылка, статус)
- ❤️ Избранное — добавление проектов в закладки
- 🔍 Фильтрация пользователей:
  - Авторы избранных проектов
  - Авторы проектов, в которых участвую
  - Пользователи, которым нравятся мои проекты
  - Участники моих проектов
- 👨‍💼 Админ-панель для управления пользователями и проектами
- 🖼️ Генерация аватарок автоматически при регистрации
- 📱 Адаптивный дизайн на Bootstrap 5

## Стек технологий

| Компонент | Технология |
|-----------|------------|
| Backend | Django 5.2 |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| База данных | SQLite (по умолчанию) |
| Формы | Django Crispy Forms + crispy-bootstrap5 |
| Работа с изображениями | Pillow (PIL) |
| Язык | Python 3.10+ |

## Установка и запуск проекта

### Требования

- Python 3.10 или выше
- pip (менеджер пакетов Python)
- Git

```bash
Шаг 1: Клонирование репозитория

git clone https://github.com/yourusername/teamfinder.git
cd teamfinder

Шаг 2: Создание виртуального окружения
Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Шаг 3: Установка зависимостей
pip install django pillow crispy-bootstrap5 django-crispy-forms

Шаг 4: Настройка переменных окружения
Создайте файл .env в корне проекта:

SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

Шаг 5: Применение миграций
python manage.py makemigrations users projects
python manage.py migrate

Шаг 6: Создание суперпользователя (для доступа в админку)

python manage.py createsuperuser

Заполните поля (пример):

Email: admin@example.com
Name: Admin
Surname: User
Phone: 1234567890
Password: admin123

Шаг 7: Запуск сервера разработки
python manage.py runserver

Шаг 8: Открыть проект в браузере
Перейдите по адресу: http://127.0.0.1:8000/

```md
teamfinder/
├── manage.py
├── db.sqlite3
├── .env
├── requirements.txt
├── README.md
├── .gitignore
├── teamfinder/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── constants.py
├── projects/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── users/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── profile_edit.html
│   │   ├── users_list.html
│   │   └── favorites_list.html
│   └── projects/
│       ├── home.html
│       ├── project_detail.html
│       └── project_form.html
├── media/
│   └── avatars/
└── static/
    └── css/
        └── style.css

URL-маршруты:

/ - Главная страница (список проектов)
/users/register/ - Регистрация
/users/login/ - Вход
/users/logout/	Выход
/users/ - Список пользователей
/users/profile/<id>/ - Профиль пользователя
/users/profile/edit/ - Редактирование профиля
/users/favorites/ - Список избранного
/users/my-projects/ - Мои проекты
/project/create/ - Создание проекта
/project/<id>/ - Детали проекта
/project/<id>/edit/ - Редактирование проекта
/admin/ - Админ-панель


Автор
Александр

GitHub: https://github.com/Dang0oo

Email: kefarag@mail.ru