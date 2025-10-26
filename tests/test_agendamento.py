import pytest
from src.paciente import Paciente
from src.medico import Medico
from src.agendamento import Agendamento

def test_confirmar_remove_horario_e_muda_status():
    p = Paciente("Ana", "12345678901")
    m = Medico("Dr. X", "Orto", agenda=["2025-10-20 10:00"])
    ag = Agendamento(p, m, "2025-10-20 10:00")
    ag.confirmar()
    assert ag.status == Agendamento.STATUS_CONFIRMADO
    assert m.disponivel("2025-10-20 10:00") is False

def test_confirmar_com_paciente_inativo_deve_levantar_erro():
    p = Paciente("Beto", "12345678901", ativo=False)
    m = Medico("Dr. Y", "Geral", agenda=["2025-10-20 11:00"])
    ag = Agendamento(p, m, "2025-10-20 11:00")
    with pytest.raises(ValueError):
        ag.confirmar()

def test_realizar_so_possivel_se_confirmado():
    p = Paciente("C", "12345678901")
    m = Medico("Dr. Z", "Geral", agenda=["2025-10-20 12:00"])
    ag = Agendamento(p, m, "2025-10-20 12:00")
    with pytest.raises(ValueError):
        ag.realizar()  # ainda não confirmado
    ag.confirmar()
    ag.realizar()
    assert ag.status == Agendamento.STATUS_REALIZADO

def test_cancelar_devolve_horario_se_confirmado():
    p = Paciente("D", "12345678901")
    m = Medico("Dr. W", "Geral", agenda=["2025-10-20 13:00"])
    ag = Agendamento(p, m, "2025-10-20 13:00")
    ag.confirmar()
    ag.cancelar()
    assert ag.status == Agendamento.STATUS_CANCELADO
    assert m.disponivel("2025-10-20 13:00") is True

def test_cancelar_apos_realizado_nao_devolve_horario():
    p = Paciente("E", "12345678901")
    m = Medico("Dr. V", "Geral", agenda=["2025-10-20 14:00"])
    ag = Agendamento(p, m, "2025-10-20 14:00")
    ag.confirmar()
    ag.realizar()
    ag.cancelar()
    assert ag.status == Agendamento.STATUS_CANCELADO
    assert m.disponivel("2025-10-20 14:00") is False