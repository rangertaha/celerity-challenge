
# Third party imports
from django import forms

# Local imports
from .roman import RomanNumeral


class RomanNumeralsForm(forms.Form):
    number = forms.IntegerField(label='Number', min_value=0, max_value=3999,
                                help_text='Enter a number between 0 to 3999')
    def __init__(self, *args, **kwargs):
            super(RomanNumeralsForm, self).__init__(*args, **kwargs)
            self.fields['number'].widget.attrs.update({'class': 'form-control'})