class Agendamento:
    STATUS_CRIADO = "CRIADO"
    STATUS_CONFIRMADO = "CONFIRMADO"
    STATUS_REALIZADO = "REALIZADO"
    STATUS_CANCELADO = "CANCELADO"

    def __init__(self, paciente, medico, horario: str):
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
        self.status = Agendamento.STATUS_CRIADO
        self._horario_removido = False
    
    def confirmar(self):
        if self.status != Agendamento.STATUS_CRIADO:
            raise ValueError("Só é possível confirmar agendamento que esteja em 'CRIADO'.")
        
        if not self.medico.disponivel(self.horario):
            raise ValueError("Médico não disponível neste horário.")
        
        if not getattr(self.paciente, "ativo", True):
            raise ValueError("Paciente inativo não pode confirma agendamento.")
        
        self.medico.remover_horario(self.horario)
        self._horario_removido = True
        self.status = Agendamento.STATUS_CONFIRMADO
    
    def realizar(self):
        if self.status != Agendamento.STATUS_CONFIRMADO:
            raise ValueError("Só é possível realizar agendamento que esteja 'CONFIRMADO'.")
        self.status = Agendamento.STATUS_REALIZADO

    def cancelar(self):
        if self.status == Agendamento.STATUS_REALIZADO:
            self.status = Agendamento.STATUS_CANCELADO
            return

        if self.status == Agendamento.STATUS_CONFIRMADO and self._horario_removido:
            if not self.medico.disponivel(self.horario):
                self.medico.adicionar_horario(self.horario)
        self._horario_removido = False

        self.status = Agendamento.STATUS_CANCELADO