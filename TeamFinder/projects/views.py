from django.views.generic import ListView
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    ordering = ['-created_at']
    paginate_by = 12
    