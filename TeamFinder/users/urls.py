from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import (
    UserListView,
    add_to_favorites,
    change_password_view,
    favorites_list,
    profile_edit_view,
    profile_view,
    register_view,
    remove_from_favorites,
    user_projects_view,
)

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),  # ИСПРАВЛЕНО
    
    path('', UserListView.as_view(), name='users_list'),

    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/change-password/', change_password_view, name='change_password'),
    
    path('my-projects/', user_projects_view, name='user_projects'),
    
    path('favorites/', favorites_list, name='favorites_list'),
    path('favorites/add/<int:project_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:project_id>/', remove_from_favorites, name='remove_from_favorites'),
]