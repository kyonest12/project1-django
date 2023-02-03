from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from blogs.models import Category
from .forms import signUpForm, editProfileForm, changePasswordForm
from django.contrib.auth.views import PasswordChangeForm, PasswordChangeView

class userRegisterForm(CreateView):
    form_class = signUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super(userRegisterForm, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

class userEditForm(UpdateView):
    form_class = editProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, *args, **kwargs):
        context = super(userEditForm, self).get_context_data(*args, **kwargs)
        context["cate_menu"] = Category.objects.all()
        return context

    def get_object(self):
        return self.request.user

class passwordChangeView(PasswordChangeView):
    form_class = changePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_change_success')

def passwordChangeSuccess(request):
    return render(request, 'registration/password_change_success.html')