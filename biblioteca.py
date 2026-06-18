import os

OPCAO_LISTAR = 1
OPCAO_EMPRESTAR = 2
OPCAO_CADASTRAR = 3
OPCAO_REMOVER = 4
CONTINUAR = 1
SAIR = 0

livros_disponiveis = []



def pagina_inicial():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 60)
    print(" " * 24 + "BIBLIOTECA")
    print("=" * 60)
    print()
    print("[1] Listar livros")
    print("[2] Pegar emprestado")
    print("[3] Cadastrar livro")
    print("[4] Remover livro")
    print("[0] Sair")
    print()
    print("=" * 60)


def deseja_continuar():
    while True:
        opc = int(input(
            "\nDeseja continuar?\n"
            "1 - Sim\n"
            "2 - Não\n"
            "Opção: "
        ))

        if opc in [CONTINUAR, SAIR]:
            os.system('cls' if os.name == 'nt' else 'clear')
            return opc

        print("Opção inválida!")


def listar_livros():
    print("\n" + "=" * 60)
    print("                     BIBLIOTECA")
    print("=" * 60)

    if not livros_disponiveis:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nNenhum livro cadastrado.\n")
        return

    print(f"\nTotal de livros: {len(livros_disponiveis)}\n")

    for indice, livro in enumerate(livros_disponiveis, start=1):
        print("-" * 60)
        print(f"Livro #{indice}")
        print("-" * 60)
        print(f"Título      : {livro['titulo']}")
        print(f"Autor       : {livro['autor']}")
        print(f"Ano         : {livro['ano']}")
        print(f"Gênero      : {livro['genero']}")
        print(f"ISBN        : {livro['isbn']}")
        print(f"Disponível  : {'Sim' if livro['disponivel'] else 'Não'}")
        print()

    print("=" * 60)


while True:
    pagina_inicial()

    opcao_menu = int(input("Opção: "))
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao_menu not in [OPCAO_LISTAR, OPCAO_EMPRESTAR, OPCAO_CADASTRAR, OPCAO_REMOVER]:
        print("Opção inválida!")
        continue

    elif opcao_menu == OPCAO_LISTAR:
        listar_livros()

        if deseja_continuar() == SAIR:
            break

    elif opcao_menu == OPCAO_CADASTRAR:
        print("Cadastrar livro")

        livros_disponiveis.append({
            "titulo": input("Digite o título do livro: "),
            "autor": input("Digite o autor: "),
            "ano": int(input("Digite o ano de publicação: ")),
            "genero": input("Digite o gênero: "),
            "isbn": input("Digite o ISBN: "),
            "disponivel": True
        })

        print(f'Livro "{livros_disponiveis[-1]["titulo"]}" cadastrado com sucesso!')

        if deseja_continuar() == SAIR:
            break

    elif opcao_menu == OPCAO_REMOVER:
        listar_livros()

        livro_escolhido = int(
            input("Digite o número do livro que deseja remover: ")
        )

        if 1 <= livro_escolhido <= len(livros_disponiveis):
            livro_removido = livros_disponiveis.pop(livro_escolhido - 1)

            print(f'Livro "{livro_removido["titulo"]}" removido com sucesso!')
        else:
            print("Livro inválido!")

        if deseja_continuar() == SAIR:
            break

    elif opcao_menu == OPCAO_EMPRESTAR:
        print("Opção emprestar")
        if deseja_continuar() == SAIR:
            break



print('Sistema encerrado.')