from django import forms
from django.contrib.auth.models import User
from .models import Post


from .models import Comment

class AddMemeForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image' ,'content']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

