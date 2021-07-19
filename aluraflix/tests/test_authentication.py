from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='c3po', password='123456')
        self.list_url = reverse('programas-list')

    def test_autenticacao_de_um_usuario_com_credenciais_corretas(self):
        """ Teste que verifica a autenticação de um usuário com as credenciais corretas """

        user = authenticate(username='c3po', password='123456')

        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """ Teste que verifica uma requisição GET sem autenticar """

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        """ Teste que verifica que o usuario não pode logar se errar o username """

        user = authenticate(username='c3pp', password='123456')

        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_de_user_com_senha_incorreta(self):
        """ Teste que verifica que o usuario não pode logar se errar a senha """

        user = authenticate(username='c3po', password='123455')

        self.assertFalse((user is not None) and user.is_authenticated)
