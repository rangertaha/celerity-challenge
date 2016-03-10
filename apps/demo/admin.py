
# Third party imports
from django.contrib import admin

# Local imports
from .models import RomanNumerals


@admin.register(RomanNumerals)
class WeatherEmailAdmin(admin.ModelAdmin):
    fields = ('email', 'city')
