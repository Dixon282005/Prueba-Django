from django.test import TestCase
from core.services.get_repos import obtener_repos_originales

class GitHubAPITest(TestCase):
    def test_obtener_repos_exito(self):
        repos = obtener_repos_originales('misterdiaz')
        self.assertIsInstance(repos, list)
        if len(repos) > 0:
            self.assertIsInstance(repos[0], str)

    def test_usuario_no_existe(self):
        repos = obtener_repos_originales('usuario_que_no_existe_123456789')
        self.assertEqual(repos, [])