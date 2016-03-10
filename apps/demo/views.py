
# Standard lib imports
import logging

# Third party imports
from django.views.generic.edit import CreateView

# Local imports
from .models import RomanNumerals
from .forms import RomanNumeralsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RomanNumeralsView(CreateView):
    model = RomanNumerals
    form_class = RomanNumeralsForm
    success_url = '/'
