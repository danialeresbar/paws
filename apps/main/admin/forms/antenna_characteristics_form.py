from django import forms

from apps.main.models import AntennaCharacteristics


class AntennaCharacteristicsModelForm(forms.ModelForm):

    class Meta:
        model = AntennaCharacteristics
        fields = ('height', 'height_type', 'height_uncertainty',)
