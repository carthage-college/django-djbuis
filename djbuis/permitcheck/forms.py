from django import forms


class SearchForm(forms.Form):
    lsearch = forms.CharField(max_length=7, required=False)
    psearch = forms.CharField(max_length=5, required=False)
    isearch = forms.CharField(max_length=7, required=False)