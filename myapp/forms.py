from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(label="", required=True, max_length=150)

SearchFormSet = forms.formset_factory(SearchForm)
