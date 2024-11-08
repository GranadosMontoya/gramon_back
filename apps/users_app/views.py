#import django
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView,TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin

#import local
from .forms import LoginForm
from .mixing_user import not_login


class Login(not_login,FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('user_app:home')       
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super(Login, self).form_valid(form)

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )
        )


class Home(LoginRequiredMixin,TemplateView):
    template_name = "users/home.html"
    login_url = reverse_lazy('user_app:login')