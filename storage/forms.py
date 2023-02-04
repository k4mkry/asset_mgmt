from django import forms
from .models import Asset


class DateInput(forms.DateInput):
    input_type = 'date'


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        # fields = [
        #     'name',
        #     'serial_number',
        #     'purchase_date',
        #     'status'
        # ]
        fields = '__all__'
        widgets = {
            'purchase_date': DateInput(),
        }
