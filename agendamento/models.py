from django.db import models
from django.contrib.auth.models import User

class Consulta(models.Model):

    OPCOES_SERVICO = [
        ("Clareamento dental", "Clareamento dental"),
        ("Facetas", "Facetas"),
        ("Lentes de Contato", "Lentes de Contato"),
        ("Tratamento de Canal", "Tratamento de Canal"),
        ("Tratamento de Gengiva", "Tratamento de Gengiva"),
    ]

    OPCOES_MES = [
        ("Junho", "Junho"),
        ("Julho", "Julho"),
        ("Agosto", "Agosto"),
    ]

    OPCOES_DIA = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    OPCOES_HORARIO = [
        ("08:00", "08:00"),
        ("08:30", "08:30"),
        ("09:00", "09:00"),
        ("09:30", "09:30"),
        ("10:00", "10:00"),
        ("10:30", "10:30"),
        ("11:00", "11:00"),
        ("11:30", "11:30"),
        ("12:00", "12:00"),
        ("12:30", "12:30"),
    ]

    servico = models.CharField(max_length=100, choices=OPCOES_SERVICO, null=False, blank=False)
    mes = models.CharField(max_length=20, choices=OPCOES_MES, null=False, blank=False)
    dia = models.IntegerField(choices=OPCOES_DIA, null=False, blank=False)
    horario = models.CharField(max_length=100, choices=OPCOES_HORARIO, null=False, blank=False)
    # cliente = models.ForeignKey(
    #     to=User,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=False,
    #     related_name='user'
    # )
    cliente = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False
    )

    def __str__(self):
        return f'serviço: {self.servico} | mês: {self.mes} | dia: {self.dia} | horário: {self.horario}'