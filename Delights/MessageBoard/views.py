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
        message_count = len(Message.objects.all())
        if message_count >= 30:
          oldest = Message.objects.first()
          oldest.delete()
        context = super().get_context_data(**kwargs)
        context['messages']= Message.objects.all().reverse()
        context['current_user']=self.request.user
        context['count']=message_count
        return context

def logout_request(request):
  logout(request)
  return redirect("login")


# This is the typical path for a view inheriting from TemplateView.

# as_view returns a function that calls dispatch.
# dispatch calls get or, if request.method isn't GET, the http_method_not_allowed method.
# get calls get_context_data and passes that as an argument to render_to_response.
# render_to_response calls get_template_names and passes that as an argument to TemplateResponse.