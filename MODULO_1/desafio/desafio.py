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
        return

    def adicionar_contato(contatos):
        print(f"{spacer}Insira os dados de contato:")
        nome = input("Nome: ")
        while True:
            telefone = input("Telefone: ")
            telefone_valido = validar_numero(telefone)
            if telefone_valido == False:
                print(f"{spacer}Numero de telefone invalido{spacer}")
            else:
                break
        while True:
            email = input("Email: ")
            email_valido = validar_email(email)
            if email_valido == False:
                print(f"{spacer}Email invalido{spacer}")
            else:
                break
        novo_contato = {"nome": nome, "telefone": telefone_valido, "email": email_valido, "favorito": False}
        contatos.append(novo_contato)
        print(f"{spacer}{nome} foi adicionado com sucesso!{spacer}")
        return
    
    def marcar_favorito(contatos, indice):
        contatos[indice]["favorito"] = True
        print(f"{spacer}Contato {contatos[indice]['nome']} foi marcado como favorito!{spacer}")
        return
    def ver_favoritos(contatos):
        print("Fav   -    Nome   -   Telefone    -   Email")
        for indice, contato in enumerate(contatos, start=1):
            if contato["favorito"]:
                favorite_icon = "[⭐]"
                print(f"{favorite_icon} {indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
        return

    def editar_contato(contatos, indice):
        contatos[indice]["nome"] = input(f"[{contatos[indice]["nome"]}\nNovo nome: ")
        contatos[indice]["telefone"] = input(f"[{contatos[indice]["telefone"]}\nNovo telefone: ")
        contatos[indice]["email"] = input(f"[{contatos[indice]["email"]}\nNovo email: ")
        print(f"{spacer}Contato editado com sucesso!{spacer}")
        return
        
    def apagar_contato(contatos, indice):
        print(f"Tem certeza que quer deletar {contatos[indice]['nome']} ? [ Y / N]")
        if input().lower() == 'y':
            deleted_user = contatos.pop(indice)
            print(f"{spacer}{deleted_user} foi deletado com sucesso!{spacer}")
        else:
            print(f"{spacer}Operação cancelada!{spacer}")
        return
    
    def validar_numero(numero):
        numero = ''.join(filter(str.isdigit, numero))
        if len(numero) == 11:
            return "({}) {}-{}".format(numero[:2], numero[2:7], numero[7:])
        elif len(numero) == 10:
            return "({}) {}-{}".format(numero[:2], numero[2:6], numero[6:]) 
        else:
            return False
    def validar_email(email):
        return email if "@" in email and "." in email else False

    selected_option = input("Selecione uma opção: ")
    try:
        if selected_option == '1':
            ver_contatos(contatos)

        elif selected_option == '2':

            adicionar_contato(contatos)

        elif selected_option == '3':
            ver_contatos(contatos)
            entrada = input("Favoritar contato: ")
            indice = int(entrada)-1
            marcar_favorito(contatos,indice)

        elif selected_option == '4':
            ver_favoritos(contatos)

        elif selected_option == '5':
            ver_contatos(contatos)
            entrada = input("Editar o contato: ")
            indice = int(entrada)-1
            editar_contato(contatos, indice) 

        elif selected_option == '6':
            ver_contatos(contatos)
            entrada = input("Deletar contato: ")
            indice = int(entrada)-1
            apagar_contato(contatos, indice) 

        elif selected_option == '7':
            print("Saindo...")
            break
    except IndexError as e:
        print(f"{spacer}Indice de contato invalido{spacer}")