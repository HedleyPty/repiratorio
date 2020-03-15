from .models import Respiratorio
from django.forms import ModelForm

class FormularioRespiratorio(ModelForm):
    class Meta:
        model =Respiratorio
        fields ="__all__"
        