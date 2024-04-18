from django.forms import ModelForm
from .models import Cycle

class CycleForm(ModelForm):
  class Meta:
    model = Cycle
    fields = ['date', 'cycle']
