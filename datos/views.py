from django.shortcuts import render, redirect
from .forms import FormularioRespiratorio


# Create your views here.
def index(request):
    if request.method=="POST":
        formulario=FormularioRespiratorio(request.POST)
        if formulario.is_valid():
            formulario.save(commit=True)
            redirect("submitted")
    else:
        formulario=FormularioRespiratorio()
    return render(request, "index.html", {"formulario": formulario})
def submitted(request):
    return render(render, "listo.html",{})