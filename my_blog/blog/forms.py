from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    """Форма отправки статьи на электронную почту"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Форма оставления комментария к посту"""

    class Meta:
        model = Comment
        fields = ("name", "email", "text")


class SearchForm(forms.Form):
    """Форма для полнотекстового поиска"""
    query = forms.CharField()
