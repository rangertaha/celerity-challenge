
# Third party imports
from django.forms import ModelForm

# Local imports
from .models import RomanNumerals


class RomanNumeralsForm(ModelForm):
    class Meta:
        model = RomanNumerals
        #fields = ['email', 'city']

