from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from constants import USERS_PAGINATE_BY
from projects.models import Project

from .forms import ProfileEditForm, RegisterForm
from .models import FavoriteProject, User


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'users/register.html', {'form': form})



class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    paginate_by = USERS_PAGINATE_BY
    ordering = ['-date_joined']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.GET.get('filter')
        
        if filter_type and self.request.user.is_authenticated:
            if filter_type == 'favorite_authors':
                favorite_projects = FavoriteProject.objects.filter(
                    user=self.request.user
                ).values_list('project_id', flat=True)
                queryset = queryset.filter(
                    owned_projects__id__in=favorite_projects
                ).distinct()
            
            elif filter_type == 'participating_authors':
                queryset = queryset.filter(
                    owned_projects__participants=self.request.user
                ).distinct()
            
            elif filter_type == 'liked_my_projects':
                my_projects = Project.objects.filter(owner=self.request.user)
                queryset = queryset.filter(
                    favorites__project__in=my_projects
                ).distinct()
            
            elif filter_type == 'my_project_participants':
                my_projects = Project.objects.filter(owner=self.request.user)
                queryset = queryset.filter(
                    participated_projects__in=my_projects
                ).distinct()
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_filter'] = self.request.GET.get('filter', '')
        return context



@login_required
def profile_view(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    projects = user_profile.owned_projects.all()
    return render(request, 'users/profile.html', {
        'user_profile': user_profile,
        'projects': projects
    })



@login_required
def profile_edit_view(request):
    form = ProfileEditForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Профиль успешно обновлён!')
        return redirect('profile', user_id=request.user.id)
    return render(request, 'users/profile_edit.html', {'form': form})



@login_required
def change_password_view(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, 'Пароль успешно изменён!')
        return redirect('profile', user_id=request.user.id)
    return render(request, 'users/change_password.html', {'form': form})



@login_required
def user_projects_view(request):
    projects = request.user.owned_projects.all()
    return render(request, 'users/my_projects.html', {'projects': projects})



@login_required
def add_to_favorites(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    FavoriteProject.objects.get_or_create(user=request.user, project=project)
    messages.success(request, f'Проект "{project.name}" добавлен в избранное')
    
    next_url = request.GET.get('next', 'home')
    return redirect(next_url)



@login_required
def remove_from_favorites(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    FavoriteProject.objects.filter(user=request.user, project=project).delete()
    messages.success(request, f'Проект "{project.name}" удалён из избранного')
    
    next_url = request.GET.get('next', 'home')
    return redirect(next_url)



@login_required
def favorites_list(request):
    favorites = FavoriteProject.objects.filter(user=request.user).select_related('project')
    return render(request, 'users/favorites_list.html', {'favorites': favorites})