from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Todo

class LogoutView(TemplateView):
    template_name = "logout-page.html"

class HomeListView(LoginRequiredMixin,ListView):
    model = Todo
    context_object_name = "dataset"
    template_name = "home.html"

class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ["title","description","date"]
    template_name = "create-todo.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TodoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Todo
    template_name = "update-todo.html"
    fields = ["title","description","date"]

    def test_func(self):
        obj = self.get_object()
        return obj

class TodoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Todo
    template_name = "delete-todo.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj