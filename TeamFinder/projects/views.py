from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import models
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from constants import PROJECTS_PAGINATE_BY

from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    ordering = ['-created_at']
    paginate_by = PROJECTS_PAGINATE_BY

    def get_queryset(self):
        return super().get_queryset().select_related('owner').annotate(
            participants_count=Count('participants')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_favorite_projects'] = self.request.user.favorites.values_list('project_id', flat=True)
        else:
            context['user_favorite_projects'] = []
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return super().get_queryset().select_related('owner').prefetch_related('participants')


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description', 'github_url', 'status']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.object.pk})  # ИСПРАВЛЕНО


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    fields = ['name', 'description', 'github_url', 'status']
    
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    
    def get_success_url(self):
        return reverse('projects:project_detail', kwargs={'pk': self.object.pk})  # ИСПРАВЛЕНО


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects:home')  # ИСПРАВЛЕНО
    
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


@login_required
def join_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user in project.participants.all():
        messages.warning(request, 'Вы уже участвуете в этом проекте')
    else:
        project.participants.add(request.user)
        messages.success(request, f'Вы присоединились к проекту "{project.name}"')
    return redirect('projects:project_detail', pk=pk)  # ИСПРАВЛЕНО


@login_required
def leave_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user not in project.participants.all():
        messages.warning(request, 'Вы не участвуете в этом проекте')
    else:
        project.participants.remove(request.user)
        messages.success(request, f'Вы вышли из проекта "{project.name}"')
    return redirect('projects:project_detail', pk=pk)  # ИСПРАВЛЕНО


@login_required
def user_projects_view(request):
    projects = request.user.owned_projects.all().select_related('owner').annotate(
        participants_count=Count('participants')
    )
    return render(request, 'users/my_projects.html', {'projects': projects})


def search_projects(request):
    query = request.GET.get('q', '')
    projects = Project.objects.all().select_related('owner').annotate(
        participants_count=Count('participants')
    )
    if query:
        projects = projects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    return render(request, 'projects/search_results.html', {
        'projects': projects,
        'query': query
    })


def filter_projects(request):
    status = request.GET.get('status', '')
    projects = Project.objects.all().select_related('owner').annotate(
        participants_count=Count('participants')
    )
    if status:
        projects = projects.filter(status=status)
    return render(request, 'projects/projects_list.html', {
        'projects': projects,
        'current_filter': status
    })