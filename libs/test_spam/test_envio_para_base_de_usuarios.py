from unittest.mock import Mock

import pytest
from spam.enviador_email import Enviador
from spam.main import EnviadorDeSpam
from spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Emerson', email='test@test.com.br'),
            Usuario(nome='Medalha', email='test2@test.com.br'),
        ],
        [
            Usuario(nome='Emerson', email='test@test.com.br'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'test@test.com.br',
        'curso de python',
        'confira os modulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_params_de_spam(sessao):
    usuario = Usuario(nome='Emerson', email='test@test.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'test2@test.com.br',
        'curso de python',
        'confira os modulos',
    )
    enviador.enviar.assert_called_once_with(
        'test2@test.com.br',
        'test@test.com.br',
        'curso de python',
        'confira os modulos',
    )
