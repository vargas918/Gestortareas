from django.forms import ModelForm
from .models import Listar

class ListarForm(ModelForm):
    class Meta:
        model = Listar
        fields = '__all__'