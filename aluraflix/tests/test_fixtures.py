from django.test import TestCase
from aluraflix.models import Programa


class FixturesDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixture(self):
        programas = Programa.objects.all()
        programa_bizarro = Programa.objects.get(pk=1)

        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(programas), 9)
