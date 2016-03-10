
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

    def clean(self):
        cleaned_data = super(RomanNumeralsForm, self).clean()
        self.cleaned_number = cleaned_data.get('number', '')

        try:
            rnum = RomanNumeral(self.cleaned_number)
        except:
            raise forms.ValidationError("You entered an invalid number")

    def msg(self):
        number = RomanNumeral(self.cleaned_number)
        return '{0} is {1}'.format(
            self.cleaned_number, number.rom)
