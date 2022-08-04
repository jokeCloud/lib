import pytest
from spam.db import Conexao
from spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Emerson', email='test@test.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Emerson', email='test@test.com.br'),
                Usuario(nome='Medalha', email='test2@test.com.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
