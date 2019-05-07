from django.shortcuts import render
from apps.forms import NotificaForm

# Create your views here.

def inputar_email(request):
    formulario = NotificaForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario = NotificaForm()
        msg = 'Pedido realizado com sucesso'
        
    contexto = {
        'form' : formulario,
        'msg' : msg
    }

    return render( request, 'index.html', contexto)