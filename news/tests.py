from django.test import TestCase
from django.urls import resolve, reverse
from news.views import home
from news.models import Giornalista
# Create your tests here.

####################################################################################################
######################################### APPROFONDIMENTO ##########################################
# Basic Testing Strategies:          https://docs.djangoproject.com/en/2.0/intro/tutorial05/
# Codici di Stato HTTP:              https://it.wikipedia.org/wiki/Codici_di_stato_HTTP
# Modello di Sviluppo Test Driven:   https://it.wikipedia.org/wiki/Test_driven_development
####################################################################################################

# lanciamo tutti i test in maniera automatizzata con "python manage.py test"
# possiamo ottenere una versione dettagliata dei test con "python manage.py test --verbosity=2"


# test sulla nostra funzione view "home" (news.views.home)
class HomeViewTests(TestCase):
    """ una prima serie di test per verificare la corretta implementazione della funzione view home """

    def test_url_resolves_home_view(self):
        """ controllo che all'url specificato come parametro di resolve, 'risponda' la funzione home """
        view = resolve("/")
        self.assertEquals(view.func, home)

    def test_home_view_url_by_name(self):
        """ controllo la possibilità di accedere alla view tramite il nome specificato nell'url, e verifico lo status code """
        url = reverse("homeview")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)



# test per il modello Giornalista (news.models.Giornalista)
class GiornalistaTestCase(TestCase):
    """ una prima serie di test per verificare la corretta implementazione del metodo Giornalista """

    def setUp(self):
         """ grazie a setUp, ciascun metodo viene testato con dati creati appositmente per il test """
        Giornalista.objects.create(nome="Guido", cognome="van Rossum")

    def test_giornalista_str(self):
        """ testiamo la corretta rappresentazione in stringa del modello Giornalista """
        giornalista = Giornalista.objects.get(nome="Guido")
        self.assertEquals(giornalista.__str__(), "Guido van Rossum")
