from django import forms

class UrlForm(forms.Form):
    long_url = forms.URLField(label='Long URL', max_length=200)