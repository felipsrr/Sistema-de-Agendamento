class Paciente:
    def __init__(self, nome: str, cpf: str, ativo: bool = True):
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo
        self._validar_cpf()
    
    def _validar_cpf(self):
        if not(isinstance(self.cpf, str) and self.cpf.isdigit() and len(self.cpf) == 11):
            raise ValueError("CPF inválido: Deve conter 11 dígitos numéricos.")