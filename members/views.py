# Create your views here.\
from django.forms import forms
from django.views.generic.edit import ProcessFormView
from theblog.models import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .froms import ProfilePageForm, UserForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
#from django.contrib.auth.forms import PasswordChangeForm
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')
class CreateProfilePage(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class =PasswordChangingForm
    template_name = 'registration/change-password.html'
    #success_url = reverse_lazy('password_success')
def password_success(request):
    return render(request, 'registration/password_success.html', {})
class UserRegistrationView(generic.CreateView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    def get_object(self):#to get the model object to the current logged in user
        return self.request.user