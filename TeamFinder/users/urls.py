from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import (
    register_view, 
    UserListView, 
    add_to_favorites, 
    remove_from_favorites, 
    favorites_list,
    profile_view,
    profile_edit_view,
    user_projects_view,
    change_password_view
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('', UserListView.as_view(), name='users_list'),

    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/change-password/', change_password_view, name='change_password'),
    
    path('my-projects/', user_projects_view, name='user_projects'),
    
    path('favorites/', favorites_list, name='favorites_list'),
    path('favorites/add/<int:project_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:project_id>/', remove_from_favorites, name='remove_from_favorites'),
]