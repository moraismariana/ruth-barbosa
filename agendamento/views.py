from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def redirecionamento(request):
    return render(request, 'agendamento/redirecionamento.html')

# agendamento
def agendamento_1(request):
    return render(request, 'agendamento/agendamento_1.html')

def agendamento_2(request):
    return render(request, 'agendamento/agendamento_2.html')

def agendamento_3(request):
    return render(request, 'agendamento/agendamento_3.html')

def agendamento_4(request):
    return render(request, 'agendamento/agendamento_4.html')

def agendamento_5(request):
    return render(request, 'agendamento/agendamento_5.html')

# reagendamento
def reagendamento_1(request):
    return render(request, 'agendamento/reagendamento_1.html')

def reagendamento_2(request):
    return render(request, 'agendamento/reagendamento_2.html')

def reagendamento_3(request):
    return render(request, 'agendamento/reagendamento_3.html')

# cancelamento
def cancelamento_1(request):
    return render(request, 'agendamento/cancelamento_1.html')

def cancelamento_2(request):
    return render(request, 'agendamento/cancelamento_2.html')