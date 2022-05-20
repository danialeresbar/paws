from django import forms

from apps.main.models import DbConfiguration


class DbConfigurationModelForm(forms.ModelForm):

    class Meta:
        model = DbConfiguration
        fields = ('maintenance_mode', 'restrict_frequency_to_TV',)
