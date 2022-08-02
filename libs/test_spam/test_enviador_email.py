import pytest
from spam.enviador_email import EmailInvalido, Enviador


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['test@test.com.br', 'foo@bar.com.br'],
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'test1@test.com.br',
        'cursos de python',
        'olow como',
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo'],
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'test1@test.com.br',
            'cursos de python',
            'olow como',
        )
