from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import register_view, UserListView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(next_page='login'),
         name='logout'),
    path('users/', UserListView.as_view(), name='users_list'),
]
