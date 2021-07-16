from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = "Procurando Ningúem em latim",
            data_lancamento = "2003-07-04",
            tipo = "F",
            likes = 2340,
            dislikes = 40
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """ Teste que verifica os campos que estão sendo serializados """

        data = self.serializer.data
        
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))
        

