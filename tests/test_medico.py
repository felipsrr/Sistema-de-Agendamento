import pytest
from src.medico import Medico

def test_adicionar_e_verificar_horario():
    m = Medico("Dr. A", "Cardio")
    m.adicionar_horario("2025-10-20 10:00")
    assert m.disponivel("2025-10-20 10:00") is True

def test_adicionar_horario_duplicado_levanta_erro():
    m = Medico("Dr. B", "Geral")
    m.adicionar_horario("2025-10-20 11:00")
    with pytest.raises(ValueError):
        m.adicionar_horario("2025-10-20 11:00")

def test_remover_horario_inexistente_levanta_erro():
    m = Medico("Dr. C", "Pediatria")
    with pytest.raises(ValueError):
        m.remover_horario("2025-10-20 12:00")