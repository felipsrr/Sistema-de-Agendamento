import pytest
from src.paciente import Paciente

def test_criar_paciente_valido():
    p = Paciente("Ana","12345678901")
    assert p.nome == "Ana"
    assert p.cpf == "12345678901"
    assert p.ativo is True

def test_cpf_inavlido_deve_levantar_erro():
    with pytest.raises(ValueError):
        Paciente("João", "123")
    with pytest.raises(ValueError):
        Paciente("Maria", "abcdef12345")