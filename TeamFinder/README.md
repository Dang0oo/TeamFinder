# TeamFinder

**TeamFinder** — это веб-платформа для поиска команды и сотрудничества в IT-проектах. Сервис помогает разработчикам находить единомышленников, создавать совместные проекты и делиться идеями.

## Основные функции

- 👤 Регистрация и авторизация пользователей
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
| Frontend | HTML, CSS, Bootstrap 5 |
| База данных | PostgreSQL 16 |
| Формы | Django Crispy Forms + crispy-bootstrap5 |
| Работа с изображениями | Pillow |
| Контейнеризация | Docker |
| Язык | Python 3.10+ |

## Установка и запуск проекта

### Требования

- Python 3.10 или выше
- pip
- Docker Desktop (для запуска PostgreSQL)


---

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/Dang0oo/teamfinder.git
cd teamfinder

Шаг 2: Создание виртуального окружения
bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

Шаг 3: Установка зависимостей
bash
pip install -r requirements.txt

Шаг 4: Настройка переменных окружения
Создайте файл .env в корне проекта:

env
SECRET_KEY=ваш-секретный-ключ
DEBUG=True
DB_NAME=teamfinder
DB_USER=postgres
DB_PASSWORD=ваш-пароль
DB_HOST=localhost
DB_PORT=5432

Шаг 5: Установка и запуск PostgreSQL через Docker

5.1. Запустить контейнер с PostgreSQL
bash
docker run -d --name teamfinder-db -e POSTGRES_PASSWORD=ваш-пароль -e POSTGRES_DB=teamfinder -p 5432:5432 postgres:16

5.2. Проверить, что контейнер запущен
bash
docker ps
Вы должны увидеть контейнер teamfinder-db в статусе Up.

5.3. Остановка контейнера (если нужно)
bash
docker stop teamfinder-db

5.4. Запуск остановленного контейнера
bash
docker start teamfinder-db

5.5. Удаление контейнера (полная очистка)
bash
docker stop teamfinder-db
docker rm teamfinder-db

5.6. Подключиться к базе внутри контейнера
bash
docker exec -it teamfinder-db psql -U postgres
В psql выполнить:

sql
\l  # Список всех баз
\c teamfinder  # Подключиться к базе teamfinder
\dt  # Список таблиц
\q  # Выйти
Шаг 6: Применение миграций
bash
python manage.py makemigrations
python manage.py migrate

Шаг 7: Создание суперпользователя
bash
python manage.py createsuperuser

Шаг 8: Запуск сервера разработки
bash
python manage.py runserver

Шаг 9: Открыть проект в браузере
Перейдите по адресу: http://127.0.0.1:8000/




Как остановить сервер
Нажмите сочетание клавиш:

bash
Ctrl + C
Работа с проектом
Как создать проект
Авторизуйтесь в системе

Нажмите кнопку "Создать проект" на главной странице

Заполните форму (название, описание, GitHub-ссылка, статус)

Нажмите "Создать проект"

Как участвовать в проекте
Перейдите на страницу проекта

Нажмите кнопку "Присоединиться к проекту"

Вы автоматически станете участником проекта



Как закрыть проект
Через веб-интерфейс:

Перейдите на страницу проекта

Нажмите кнопку "Редактировать" (только для автора проекта)

В поле "Статус" выберите "Закрыт"

Нажмите "Сохранить изменения"

Через админ-панель:

Перейдите в админ-панель: /admin/

Выберите раздел "Проекты"

Найдите нужный проект и откройте его

В поле "Статус" выберите "Закрыт"

Нажмите "Сохранить"

Важно: Закрытый проект не отображается в поиске и фильтрации, но остается доступен по прямой ссылке.



Управление базой данных

Как очистить базу данных
Вариант 1: Через Docker (рекомендуемый)
bash
# Удалить базу внутри контейнера
docker exec -it teamfinder-db psql -U postgres -c "DROP DATABASE IF EXISTS teamfinder;"

# Создать базу заново
docker exec -it teamfinder-db psql -U postgres -c "CREATE DATABASE teamfinder;"
bash
# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
Вариант 2: Удалить и создать контейнер заново
bash
# Остановить и удалить контейнер
docker stop teamfinder-db
docker rm teamfinder-db

# Создать новый контейнер
docker run -d --name teamfinder-db -e POSTGRES_PASSWORD=ваш-пароль -e POSTGRES_DB=teamfinder -p 5432:5432 postgres:16
bash
# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
Вариант 3: Подключиться к psql внутри контейнера
bash
docker exec -it teamfinder-db psql -U postgres
В psql выполнить:

sql
DROP DATABASE IF EXISTS teamfinder;
CREATE DATABASE teamfinder;
\q
Вариант 4: Полный сброс миграций (Linux/Mac)
bash
# Удалить все миграции кроме __init__.py
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Создать новые миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
Вариант 5: Полный сброс миграций (Windows PowerShell)
powershell
# Удалить все миграции кроме __init__.py
Get-ChildItem -Path . -Recurse -Include "*.py" -Exclude "__init__.py" | Where-Object { $_.Directory.Name -eq "migrations" } | Remove-Item
Get-ChildItem -Path . -Recurse -Include "*.pyc" | Where-Object { $_.Directory.Name -eq "migrations" } | Remove-Item

# Создать новые миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
Вариант 6: Полный сброс миграций (Windows CMD)
cmd
# Удалить все миграции кроме __init__.py
del /s /q migrations\*.py
del /s /q migrations\*.pyc

# Создать новые миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Создать суперпользователя
python manage.py createsuperuser
Вариант 7: Очистка через Django shell
bash
python manage.py shell
python
from users.models import User, FavoriteProject
from projects.models import Project

# Удалить все проекты
Project.objects.all().delete()

# Удалить все избранное
FavoriteProject.objects.all().delete()

# Удалить всех пользователей (кроме суперпользователя)
User.objects.filter(is_superuser=False).delete()
Вариант 8: Сброс конкретного приложения
bash
# Сбросить миграции для приложения users
python manage.py migrate users zero
python manage.py makemigrations users
python manage.py migrate users

# Сбросить миграции для приложения projects
python manage.py migrate projects zero
python manage.py makemigrations projects
python manage.py migrate projects



Структура проекта
text
teamfinder/
├── manage.py
├── .env
├── requirements.txt
├── README.md
├── .gitignore
├── teamfinder/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── constants.py
│   └── validators.py
├── users/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── managers.py
├── projects/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
├── templates/
│   ├── base.html
│   ├── users/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   ├── profile_edit.html
│   │   ├── change_password.html
│   │   ├── users_list.html
│   │   ├── favorites_list.html
│   │   └── my_projects.html
│   └── projects/
│       ├── home.html
│       ├── project_detail.html
│       ├── project_form.html
│       ├── project_confirm_delete.html
│       ├── search_results.html
│       └── projects_list.html
├── media/
│   └── avatars/
└── static/
    └── css/
        └── style.css



URL-маршруты
URL - Назначение
/	Главная страница - (список проектов)
/users/register/ - Регистрация
/users/login/ - Вход
/users/logout/ - Выход
/users/ - Список пользователей
/users/profile/<id>/ - Профиль пользователя
/users/profile/edit/ - Редактирование профиля
/users/profile/change-password/ - Смена пароля
/users/favorites/ - Список избранного
/users/my-projects/ - Мои проекты
/project/create/ - Создание проекта
/project/<id>/ - Детали проекта
/project/<id>/edit/ - Редактирование проекта
/project/<id>/delete/ - Удаление проекта
/project/<id>/join/ - Присоединиться к проекту
/project/<id>/leave/ - Выйти из проекта
/search/ - Поиск проектов
/filter/ - Фильтрация проектов
/admin/ - Админ-панель



Автор:
Александр

GitHub: https://github.com/Dang0oo

Email: kefarag@mail.ru