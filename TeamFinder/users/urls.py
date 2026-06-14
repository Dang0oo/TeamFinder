from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import register_view, UserListView, add_to_favorites, remove_from_favorites, favorites_list

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(next_page='login'),
         name='logout'),
    path('', UserListView.as_view(), name='users_list'),
    path('favorites/', favorites_list, name='favorites_list'),
    path('favorites/add/<int:project_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:project_id>/', remove_from_favorites, name='remove_from_favorites'),
]