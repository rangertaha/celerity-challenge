
# Standard lib imports
import logging

# Third party imports
from django.views.generic.edit import FormView
from django.contrib import messages

# Local imports
from .forms import RomanNumeralsForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RomanNumeralsView(FormView):
    template_name = 'demo/form.html'
    form_class = RomanNumeralsForm
    success_url = '/'

    def form_valid(self, form):
        if form.is_valid():
            messages.add_message(self.request, messages.SUCCESS, form.msg())
        else:
            logger.warn('Invalid input parameters')
        return super(RomanNumeralsView, self).form_valid(form)
