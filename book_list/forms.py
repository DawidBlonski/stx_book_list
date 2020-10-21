from django import forms

class ApiForms(forms.Form):
    key_words = forms.CharField(
        max_length=50,
    )
    title = forms.CharField(
        max_length=50,
        required=False,
    )
    author = forms.CharField(
        max_length=50,
        required=False,
    )
