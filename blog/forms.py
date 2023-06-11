# whenever you want to put something in the database, you put it inside forms.py
# thia is what affects the frontside of the post

from django import forms
from . models import PostModel, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = PostModel
        fields = ('title', 'content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    # label='' removes the heading "content" in the comment section
    content = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Add comment here....'}))

    class Meta:
        model = Comment
        fields = ('content',)
