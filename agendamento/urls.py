from django.urls import path
from agendamento.views import index, redirecionamento, agendamento_1, agendamento_2, agendamento_3, agendamento_4, agendamento_5, reagendamento_1, reagendamento_2, reagendamento_3, cancelamento_1, cancelamento_2

urlpatterns = [
    path('', index, name='index'),
    path('redirecionamento', redirecionamento, name='redirecionamento'),

    path('agendamento/1', agendamento_1, name='agendamento_1'),
    path('agendamento/2', agendamento_2, name='agendamento_2'),
    path('agendamento/3', agendamento_3, name='agendamento_3'),
    path('agendamento/4', agendamento_4, name='agendamento_4'),
    path('agendamento/5', agendamento_5, name='agendamento_5'),

    path('reagendamento/1', reagendamento_1, name='reagendamento_1'),
    path('reagendamento/2', reagendamento_2, name='reagendamento_2'),
    path('reagendamento/3', reagendamento_3, name='reagendamento_3'), 

    path('cancelamento/1', cancelamento_1, name='cancelamento_1'),
    path('cancelamento/2', cancelamento_2, name='cancelamento_2'),
]