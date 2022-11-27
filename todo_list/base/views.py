from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Task

#form of user authentification

class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields = '__all__'
    redirect_authentification_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


# ListView is supposed to send back a querySet of data 
class TaskList(ListView):
    model=Task
    context_object_name='tasks'

# DetailView
class TaskDetail(DetailView):
    model=Task
    context_object_name ='task'
    template_name='base/task.html'

#CreateView
class TaskCreate(CreateView):
    model=Task
    fields = '__all__'
    success_url=reverse_lazy('tasks')

#Modify the data
class TaskUpdate(UpdateView):
    model =Task
    fields = '__all__'
    success_url=reverse_lazy('tasks')

#Delete view for items
class TaskDelete(DeleteView):
    model=Task
    context_object_name = 'task'
    success_url=reverse_lazy('tasks')


