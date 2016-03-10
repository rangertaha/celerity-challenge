
# Third party imports
from django.conf.urls import url

# Local imports
from .views import RomanNumeralsView


urlpatterns = [
    url(r'^$', RomanNumeralsView.as_view(), name='weather-email')
]
