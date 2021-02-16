from django.urls import path

from .views import FilmDetailViewCB, FilmListView, home #articoloDetailView,

urlpatterns = [
    path("", home, name="homeview"),
    # path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    path("film/<int:pk>", FilmDetailViewCB.as_view(), name="film_detail"),
    path("lista_film/", FilmListView.as_view(), name="lista_film")

]
