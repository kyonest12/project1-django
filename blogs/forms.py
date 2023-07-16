from django import forms
from blogs.models import *

class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'category', 'summary', 'content', 'user', 'image')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'category' : forms.Select(attrs={'class' : 'form-control'}),
            'summary' : forms.Textarea(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '' , 'id': 'user_id', 'type' : 'hidden'}),

        }

class editForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'category', 'summary', 'content', 'image')
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'category' : forms.Select(attrs={'class' : 'form-control'}),
            'summary' : forms.Textarea(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
        error_messages = {
            'name': {
                'unique': ("Đã tồn tài thể loại này!!!"),
            },
        }

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url', 'user')
        widgets = {
            'bio' : forms.Textarea(attrs={'class' : 'form-control'}),
            'facebook_url' : forms.TextInput(attrs={'class' : 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'twitter_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control',
                                           'value': '', 'id': 'user_id', 'type' : 'hidden'})
        }

class editprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'instagram_url', 'twitter_url')
        widgets = {
            'bio' : forms.Textarea(attrs={'class' : 'form-control'}),
            'facebook_url' : forms.TextInput(attrs={'class' : 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class' : 'form-control'}),
            'twitter_url' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class createCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('blog', 'body', 'user')
        labels = {
            'body': '',
        }
        widgets = {
            'blog': forms.TextInput(attrs={'type': 'hidden', 'class': 'form-control', 'value': '', 'id': 'blog_id'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'cols' : 2, 'rows' : 3, 'placeholder' : 'Nhập bình luận'}),
            'user': forms.TextInput(attrs={'type': 'hidden', 'class': 'form-control', 'value': '', 'id': 'user_id'}),
        }
