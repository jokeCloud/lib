import pytest
from spam.db import Conexao
from spam.modelos import Usuario


# setup and tear down
@pytest.fixture
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Emerson')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Emerson'), Usuario(nome='Medalha')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()