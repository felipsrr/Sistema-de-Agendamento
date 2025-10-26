from typing import List

class Medico:
    def __init__(self, nome: str, especialidade: str, agenda: List[str] = None):
        self.nome = nome
        self.especialidade = especialidade
        self.agenda = list(agenda) if agenda else[]
    
    def adicionar_horario(self, horario: str):
        if self.disponivel(horario):
            raise ValueError(f"Horário já existe na agenda: {horario}")
        self.agenda.append(horario)

    def remover_horario(self, horario: str):
        try:
            self.agenda.remove(horario)
        except ValueError:
            raise ValueError(f"Horário não encontrado na agenda: {horario}")
    
    def disponivel(self, horario: str) -> bool:
        return horario in self.agenda
