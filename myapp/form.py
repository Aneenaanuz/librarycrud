from django import forms
from myapp.models import Library

class LibraryForm(forms.ModelForm):
    class Meta:
        model=Library
        fields="__all__"
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "category":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),

        }
