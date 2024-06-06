from django import forms
from agendamento.models import Consulta

class ConsultaForms(forms.ModelForm):
    class Meta:
        model = Consulta
        exclude = ['cliente']
        labels = {
            'mes': 'Mês',
            'horario': 'Horário',
            'servico': 'Serviço',
        }

        widgets = {
            'servico': forms.Select(attrs={'class': 'select'}),
            'mes': forms.Select(attrs={'class': 'select'}),
            'dia': forms.Select(attrs={'class': 'select'}),
            'horario': forms.Select(attrs={'class': 'select',
                                           'max-height': '100px', 'style': 'overflow-y: auto'}),
            'cliente': forms.HiddenInput(),
        }        