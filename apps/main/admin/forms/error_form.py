from django import forms

from apps.main.models import Error


class ErrorModelForm(forms.ModelForm):

    class Meta:
        model = Error
        fields = '__all__'
