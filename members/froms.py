from django.forms import widgets
from theblog.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
#for working with auth model we need to design our widget in this way
class UserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)#overridding the UserCreationForm fields
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password')
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", "type":"password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", "type":"password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", "type":"password"}))
    class Meta:
        model = User
        fields = ('old_passowrd', 'new_password1' ,'new_password2' )
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url']
        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control','placeholder':'This is placeholder'}),
            #'profile_pic':forms.TextInput(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
            'pinterest_url':forms.TextInput(attrs={'class':'form-control'}),
        }
    