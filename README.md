# 📌 Desafio 01 - Agenda em Python

## 📖 Introdução

Este repositório contém a solução para o **Desafio 01** do módulo "Introdução ao Python". O objetivo é desenvolver uma agenda de contatos funcional no terminal, aplicando conceitos fundamentais da linguagem Python.

## 🎯 Objetivo do Desafio

Criar uma aplicação em Python que permita:
- 📌 Adicionar contatos com nome, telefone e e-mail.
- ✏️ Editar informações de um contato existente.
- 📋 Listar todos os contatos cadastrados.
- ⭐ Marcar ou desmarcar contatos como favoritos.
- 📂 Exibir uma lista de contatos favoritos.
- ❌ Remover contatos da agenda.

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3**
- 📜 Manipulação de listas e dicionários
- ⌨️ Entrada e saída de dados no terminal
- 🔄 Estruturas de repetição e decisão

## 🚀 Como Executar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/desafio-agenda-python.git
   ```
2. **Acesse o diretório do projeto:**
   ```bash
   cd desafio-agenda-python
   ```
3. **Execute o script Python:**
   ```bash
   python agenda.py
   ```

## 📂 Estrutura do Projeto

```
📁 desafio-agenda-python
 ├── 📄 agenda.py  # Arquivo principal do projeto
 ├── 📄 README.md  # Documentação do desafio
```

## 📜 Código Principal

Aqui está a implementação da agenda:

```python
contatos = []

while True:
    spacer = f"\n{'='*40}\n"
    print("""
================= Agenda ===================
    1 - Ver Contatos
    2 - Cadastrar Novo Contato
    3 - Marcar como Favorito
    4 - Ver Lista de Contatos Favoritos
    5 - Editar Contato
    6 - Apagar Contato
    7 - Sair
============================================
""")

    def ver_contatos(contatos):
        if not contatos:
            print(f"{spacer}Nenhum contato cadastrado.{spacer}")
            return
        
        print(f"{spacer}Lista de Contatos:")
        print("Fav   -    Nome   -   Telefone    -   Email")
        for indice, contato in enumerate(contatos, start=1):
            favorite_icon = "[⭐]" if contato["favorito"] else "[  ]"
            print(f"{favorite_icon} {indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
        print(spacer)

    def adicionar_contato(contatos):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        novo_contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
        contatos.append(novo_contato)
        print(f"{spacer}{nome} foi adicionado com sucesso!{spacer}")
```
