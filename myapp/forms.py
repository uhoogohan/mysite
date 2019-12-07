from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(label="", required=False, max_length=150)
