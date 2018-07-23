from django.shortcuts import render, redirect
from .forms import VisitanteForm


def visitante_new(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.save()
            return redirect(visitante_new)

    else:
        form = VisitanteForm()

    return render(request, 'registro/new.html', {'form': form})
