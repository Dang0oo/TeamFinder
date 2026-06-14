from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import RegisterForm
from .models import User


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
