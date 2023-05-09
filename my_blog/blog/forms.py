from django import forms


class EmailPostForm(forms.Form):
    """Форма отправки статьи на электронную почту"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)
