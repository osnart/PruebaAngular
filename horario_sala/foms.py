from django import forms
from horario_sala.models import HoraSala


class HorarioSalaForm(forms.ModelForm):
    class Meta:
        model = HoraSala
        exclude = ()