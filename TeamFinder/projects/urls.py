from django.urls import path

from projects.views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    filter_projects,
    join_project,
    leave_project,
    search_projects,
    user_projects_view,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    
    # Участие в проекте
    path('project/<int:pk>/join/', join_project, name='join_project'),
    path('project/<int:pk>/leave/', leave_project, name='leave_project'),
    
    # Проекты пользователя
    path('my-projects/', user_projects_view, name='user_projects'),
    
    # Поиск и фильтрация
    path('search/', search_projects, name='search_projects'),
    path('filter/', filter_projects, name='filter_projects'),
]