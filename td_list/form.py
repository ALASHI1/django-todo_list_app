from django import forms
from . models import TdList


class TdForm(forms.ModelForm):
    class Meta:
        model = TdList
        fields = ('title',)



