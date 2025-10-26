# 🩺 Sistema de Agendamento de Consultas Médicas

Projeto desenvolvido em **Python**, com o objetivo de simular o funcionamento de um sistema de agendamento de consultas médicas.  
O sistema permite cadastrar pacientes e médicos, gerenciar horários e controlar o fluxo de um agendamento: **criação, confirmação, realização e cancelamento**.

---

## 🧠 Objetivo do Projeto

O projeto foi desenvolvido como atividade acadêmica para praticar:
- Programação Orientada a Objetos (POO) em Python;
- Boas práticas de testes automatizados com **pytest**;
- Controle de versões com **Git** e **GitHub**;
- Aplicação de regras de negócio e validação de dados.

---

## 🗂️ Estrutura do Projeto

Sistema-de-Agendamento/
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│ ├── paciente.py
│ ├── medico.py
│ └── agendamento.py
└── tests/
├── test_paciente.py
├── test_medico.py
└── test_agendamento.py

markdown
Copiar código

### 📁 Descrição dos diretórios
- **src/** → código principal (classes e regras de negócio)
- **tests/** → testes automatizados para cada classe
- **requirements.txt** → dependências do projeto
- **.gitignore** → arquivos que o Git deve ignorar
- **README.md** → este arquivo com a documentação

---

## ⚙️ Instalação e Execução

### 1️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv env
Ativar o ambiente:

Windows (cmd):

bash
Copiar código
env\Scripts\activate
Linux/macOS:

bash
Copiar código
source env/bin/activate
2️⃣ Instalar dependências
bash
Copiar código
pip install -r requirements.txt
Esse comando instala o pytest, pytest-cov e pytest-html, usados para testes e relatórios.

3️⃣ Executar testes automatizados
bash
Copiar código
pytest
4️⃣ Ver cobertura de código no terminal
bash
Copiar código
pytest --cov=src --cov-report=term-missing
5️⃣ Gerar relatório HTML de cobertura
bash
Copiar código
pytest --cov=src --cov-report=html
O resultado será criado na pasta htmlcov/ — abra o arquivo index.html no navegador.

6️⃣ Gerar relatório de testes em HTML (visual)
bash
Copiar código
pytest --html=report.html --self-contained-html
Abra o arquivo report.html no navegador para visualizar os testes executados.

🧩 Principais Classes e Regras de Negócio
🧍‍♀️ Paciente
Arquivo: src/paciente.py

Atributos: nome, cpf, ativo

Validação: CPF deve conter 11 dígitos numéricos

Se o CPF for inválido → lança ValueError

🩺 Médico
Arquivo: src/medico.py

Atributos: nome, especialidade, agenda

Métodos principais:

adicionar_horario(horario)

remover_horario(horario)

disponivel(horario)

Regras:

Não permitir horários duplicados

Lançar erro se tentar remover horário inexistente

📅 Agendamento
Arquivo: src/agendamento.py

Estados possíveis: CRIADO, CONFIRMADO, REALIZADO, CANCELADO

Regras:

Só pode confirmar se o paciente estiver ativo e o médico disponível

Ao confirmar, o horário é removido da agenda do médico

Ao cancelar um agendamento confirmado, o horário é liberado novamente

Se o agendamento já foi realizado, o horário não é devolvido

🧪 Testes Automatizados
Os testes garantem que todas as regras de negócio funcionem corretamente.

Arquivo	O que testa	Exemplos
test_paciente.py	Validação de CPF	CPF com letras, tamanho incorreto
test_medico.py	Agenda do médico	Adição, remoção e duplicidade de horários
test_agendamento.py	Fluxo completo	Confirmar, realizar e cancelar agendamento

💻 Comandos úteis de Git e GitHub
Inicializar repositório local
bash
Copiar código
git init
Adicionar arquivos
bash
Copiar código
git add .
Criar commit
bash
Copiar código
git commit -m "Versão inicial do Sistema de Agendamento"
Adicionar repositório remoto
bash
Copiar código
git remote add origin https://github.com/SEU-USUARIO/Sistema-de-Agendamento.git
Enviar para o GitHub
bash
Copiar código
git branch -M main
git push -u origin main
📚 Tecnologias utilizadas
🐍 Python 3.11+

🧪 pytest, pytest-cov, pytest-html

🧰 Git e GitHub para versionamento

🧠 Programação Orientada a Objetos

✨ Autor
Felipe Gabriel Silva Serrão
Estudante de Análise e Desenvolvimento de Sistemas
📅 Trabalho prático de Python — Faculdade (2025)