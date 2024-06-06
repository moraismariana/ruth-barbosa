from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from agendamento.models import Consulta
from agendamento.forms import ConsultaForms

def index(request):
    return render(request, 'index.html')

def redirecionamento(request):
    return render(request, 'agendamento/redirecionamento.html')

# agendamento
def agendamento_1(request):
    if not request.user.is_authenticated:
        return redirect('redirecionamento')
    
    if request.method == 'POST':
        form = ConsultaForms(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)  # Não salva ainda no banco de dados
            consulta.cliente = request.user  # Define o cliente como o usuário logado
            consulta.save()  # Agora salva no banco de dados
            return redirect('agendamento_5')
    else:
        form = ConsultaForms(initial={'cliente': request.user.id})  # Inicializa o formulário com o cliente

    return render(request, 'agendamento/agendamento_1.html', {'form': form})

def agendamento_2(request):
    return render(request, 'agendamento/agendamento_2.html')

def agendamento_3(request):
    return render(request, 'agendamento/agendamento_3.html')

def agendamento_4(request):
    return render(request, 'agendamento/agendamento_4.html')

def agendamento_5(request):
    return render(request, 'agendamento/agendamento_5.html')

# reagendamento
def reagendamento_1(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    form = ConsultaForms(instance=consulta)
    # form.fields.pop('servico')

    consultas = Consulta.objects.filter(cliente=request.user.id)

    if request.method == 'POST':
        form = ConsultaForms(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('pagina_usuario')

    return render(request, 'agendamento/reagendamento_1.html', {'form': form, 'consulta_id': consulta_id, 'cards': consultas})

def reagendamento_2(request):
    return render(request, 'agendamento/reagendamento_2.html')

def reagendamento_3(request):
    return render(request, 'agendamento/reagendamento_3.html')

# cancelamento
def cancelamento_1(request, consulta_id):
    consulta = Consulta.objects.get(id=consulta_id)

    consultas = Consulta.objects.filter(cliente=request.user.id)

    if request.method == 'POST':
        consulta.delete()
        return redirect('cancelamento_2')

    return render(request, 'agendamento/cancelamento_1.html', {'consulta_id': consulta_id, 'cards': consultas})

def cancelamento_2(request):
    consultas = Consulta.objects.filter(cliente=request.user.id)
    return render(request, 'agendamento/cancelamento_2.html' , {'cards': consultas})