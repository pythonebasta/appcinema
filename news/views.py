from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Film, Regista

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Homepage!</h1>")

# def home(request):
#     a = []
#     g = []
#     for art in Articolo.objects.all():
#         a.append(art.titolo)
#
#     for gio in Giornalista.objects.all():
#         g.append(gio.nome)
#
#     response = str(a) + "<br>" + str(g)
#     print(response)
#
#     return HttpResponse("<h1>" + response + "</h1>")

# def home(request):
#     a = ""
#     g = ""
#     for art in Articolo.objects.all():
#         a += (art.titolo + "<br>")
#
#     for gio in Giornalista.objects.all():
#         g += (gio.nome + "<br>")
#     response = "Articoli:<br>" + a + "<br>Giornalisti:<br>" + g
#
#     return HttpResponse("<h1>" + response + "</h1>")

def home(request):
    film = Film.objects.all()
    registi = Regista.objects.all()
    context = {"film": film, "registi": registi}
    print(context)
    return render(request, "homepage.html", context)

# def articoloDetailView(request, pk):
#     # articolo = Articolo.objects.get(pk=pk)
#     articolo = get_object_or_404(Articolo, pk=pk)
#     context = {"articolo": articolo}
#     return render(request, "articolo_detail.html", context)


### GCBV Generic Class Based Views
# Documentazione Ufficiale: https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class FilmDetailViewCB(DetailView):
    model = Film
    template_name = "film_detail.html"


class FilmListView(ListView):
    model = Film
    template_name = "lista_film.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["film"] = Film.objects.all()
        return context
