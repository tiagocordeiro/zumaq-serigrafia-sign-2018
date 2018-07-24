from django.shortcuts import render, redirect
from .forms import VisitanteForm
from .models import Visitante


def visitante_new(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.save()
            return redirect(visitante_cadastrado)

    else:
        form = VisitanteForm()

    return render(request, 'registro/new.html', {'form': form})


def visitante_cadastrado(request):
    return render(request, 'registro/thanks.html')


def visitante_sorteio(request):
    visitantes = Visitante.objects.all()
    return render(request, 'registro/sorteio.html', {'visitantes': visitantes})


def visitante_sorteio_result(request):
    visitantes = Visitante.objects.all().order_by('?')[:1]
    return render(request, 'registro/sorteio_result.html',
                  {'visitantes': visitantes})
