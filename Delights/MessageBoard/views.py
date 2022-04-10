from django.shortcuts import render
from django.views.generic.edit import CreateView
from MessageBoard.models import Message
from MessageBoard.forms import MessageForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout,login
from .forms import CreateUserForm
# Create your views here.


class SignUp(CreateView):
  form_class = CreateUserForm
  success_url = reverse_lazy("messages")
  template_name = "Registration/signup.html"
  


class MessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'MessageBoard/messages.html'
    success_url = reverse_lazy("messages")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['messages']= Message.objects.all().reverse()
        context['current_user']=self.request.user
        return context

def logout_request(request):
  logout(request)
  return redirect("login")
