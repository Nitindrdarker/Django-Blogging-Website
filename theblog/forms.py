from django import forms
from django.db.models import fields
from .models import Post, Category, Comment
#choices = [("coding", 'coding'), ("sports", "sports"), ("entertainment", "entertainemnt")]
choices = Category.objects.all().values_list("name", "name")
choice_list = [item for item in choices]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'Snippet', 'header_image')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is placeholder'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'user_name', 'type':'hidden'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'Snippet':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'Snippet')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is placeholder'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'Snippet':forms.Textarea(attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
