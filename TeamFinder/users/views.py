from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import RegisterForm
from .models import User, FavoriteProject
from projects.models import Project

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    paginate_by = 12
    ordering = ['-date_joined']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.GET.get('filter')
        
        if filter_type and self.request.user.is_authenticated:
            if filter_type == 'favorite_authors':
                # Авторы избранных проектов
                favorite_projects = FavoriteProject.objects.filter(user=self.request.user).values_list('project_id', flat=True)
                queryset = queryset.filter(projects__id__in=favorite_projects).distinct()
            
            elif filter_type == 'participating_authors':
                queryset = queryset.filter(projects__participants=self.request.user).distinct()
            
            elif filter_type == 'liked_my_projects':
                # Пользователи, которым нравятся мои проекты
                my_projects = Project.objects.filter(author=self.request.user)
                queryset = queryset.filter(favorites__project__in=my_projects).distinct()
            
            elif filter_type == 'my_project_participants':
                # Участники моих проектов
                my_projects = Project.objects.filter(author=self.request.user)
                queryset = queryset.filter(projects__in=my_projects).distinct()
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_filter'] = self.request.GET.get('filter', '')
        return context

@login_required
def add_to_favorites(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    FavoriteProject.objects.get_or_create(user=request.user, project=project)
    messages.success(request, f'Проект "{project.title}" добавлен в избранное')
    
    next_url = request.GET.get('next', 'home')
    return redirect(next_url)

@login_required
def remove_from_favorites(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    FavoriteProject.objects.filter(user=request.user, project=project).delete()
    messages.success(request, f'Проект "{project.title}" удалён из избранного')
    
    next_url = request.GET.get('next', 'home')
    return redirect(next_url)

@login_required
def favorites_list(request):
    favorites = FavoriteProject.objects.filter(user=request.user).select_related('project')
    return render(request, 'users/favorites_list.html', {'favorites': favorites})