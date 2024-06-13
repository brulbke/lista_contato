agenda = []

def adicionarContato(agenda, nome, telefone, email, favorito):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    agenda.append(contato)
    print(f"\nContato {contato['nome']} adicionado a sua agenda!\n")
    #print(agenda)
    return

def vizualizarContato(agenda):
    for indice, contato in enumerate(agenda, start=1):
        contato_favoritado = " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        if contato["favorito"] == True:
            contato_favoritado = "✓"
        else:
            contato_favoritado = " "
        print(f"{indice} [{contato_favoritado}] {nome} {telefone}/{email}")
    return
    
def editarContato(agenda, nome, telefone, email, favorito, indice):
    indice_correto = int(indice) - 1
    if indice_correto >= 0 and indice_correto < len(agenda):
        agenda[indice_correto]["nome"] = nome
        agenda[indice_correto]["telefone"] = telefone
        agenda[indice_correto]["email"] = email
        agenda[indice_correto]["favorito"] = favorito
        if favorito == "S":
            favorito = True
        elif favorito == "N":
            favorito = False
        print("\nContato editado com sucesso!\n")
        vizualizarContato(agenda)
    else:
        print("\nIndice inválido!\n")
    return

def marcarFavorito(agenda, indice):
    indice_correto = int(indice) - 1
    if indice_correto >= 0 and indice_correto < len(agenda):
        agenda[indice_correto]["favorito"] = True
        print("\nContato favoritado com sucesso!\n")
        vizualizarContato(agenda)
    else:
        print("\nIndice inválido!\n")
    return

#mudanca

def desmarcarFavorito(agenda, indice):
    indice_correto = int(indice) - 1
    if indice_correto >= 0 and indice_correto < len(agenda):
        agenda[indice_correto]["favorito"] = False
        print("\nContato retirado dos favoritos com sucesso!\n")
        vizualizarContato(agenda)
    else:
        print("\nIndice inválido!\n")
    return

def listarFavorito(agenda):
    for indice, contato in enumerate(agenda, start=1):
        if contato["favorito"] == True:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice} [✓] {nome} {telefone}/{email}")
    return
        
def deletarContato(agenda, indice):
    indice_correto = int(indice) - 1
    if indice_correto >= 0 and indice_correto < len(agenda):
        agenda.remove(agenda[indice_correto])
        print("\nContato deletado\n")
    return


while True:
    print("1. Adicionar um novo contato.")
    print("2. Vizualizar lista de contatos.")
    print("3. Editar contato.")
    print("4. Marcar contato como favorito.")
    print("5. Desmarcar contato como favorito.")
    print("6. Vizualizar lista de contatos favoritos.")
    print("7. Deletar contato.")
    print("8. Sair.")

    menu = input("\nEscolha a opção do menu: ")

    if menu == "1":
        nome = input("\nDigite o nome do contato: ")
        telefone = input("\nDigite o telefone do contato: ")
        email = input("\nDigite o email do contato: ")
        favorito = input("\nDigite S ou N para favoritar o contato: ")
        if favorito == "S":
            favorito = True
        elif favorito == "N":
            favorito = False
        adicionarContato(agenda, nome, telefone, email, favorito)
    elif menu == "2":
        vizualizarContato(agenda)
    elif menu == "3":
        indice = input("\nDigite o indice ")
        nome = input("\nDigite o novo nome: ")
        email = input("\nDigite o novo email: ")
        telefone = input("\nDigite o novo telefone: ")
        favorito = input("\nDigite S ou N para favoritar o contato: ")
        editarContato(agenda, nome, telefone, email, favorito, indice)
    elif menu == "4":
        indice = input("\nDigite o indice: ")
        marcarFavorito(agenda, indice)
    elif menu == "5":
        indice = input("\nDigite o indice: ")
        desmarcarFavorito(agenda, indice)
    elif menu == "6":
        listarFavorito(agenda)
    elif menu == "7":
        indice = input("\nDigite o indice: ")
        deletarContato(agenda, indice)
    elif menu == "8":
        print("\nAgenda fechada\n")
        break
