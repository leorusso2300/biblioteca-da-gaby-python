import os

OPCAO_LISTAR = 1
OPCAO_CADASTRAR = 2
OPCAO_REMOVER = 3
CONTINUAR = 1
SAIR = 2

livros_disponiveis = [
    "Orgulho e Preconceito",
    "Dom Casmurro",
    "O Morro dos Ventos Uivantes",
    "Jane Eyre",
    "Como Eu Era Antes de Você"
]
]


def pagina_inicial():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
========================================
             BIBLIOTECA DA GABY
========================================
Escolha uma das opções:

1 - Livros disponíveis
2 - Cadastrar livro
3 - Remover livro

========================================
""")


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
    print("Livros disponíveis:")

    for indice, livro in enumerate(livros_disponiveis, start=1):
        print(f"{indice} - {livro}")


while True:
    pagina_inicial()

    opcao_menu = int(input("Opção: "))

    if opcao_menu not in [OPCAO_LISTAR, OPCAO_CADASTRAR, OPCAO_REMOVER]:
        print("Opção inválida!")
        continue

    elif opcao_menu == OPCAO_LISTAR:
        listar_livros()

        if deseja_continuar() == SAIR:
            break

    elif opcao_menu == OPCAO_CADASTRAR:
        print("Cadastrar livro")

        titulo_livro = input("Digite o título do livro: ")

        livros_disponiveis.append(titulo_livro)

        print(f'Livro "{titulo_livro}" cadastrado com sucesso!')

        if deseja_continuar() == SAIR:
            break

    elif opcao_menu == OPCAO_REMOVER:
        listar_livros()

        livro_escolhido = int(
            input("Digite o número do livro que deseja remover: ")
        )

        if 1 <= livro_escolhido <= len(livros_disponiveis):
            livro_removido = livros_disponiveis.pop(livro_escolhido - 1)

            print(f'Livro "{livro_removido}" removido com sucesso!')
        else:
            print("Livro inválido!")

        if deseja_continuar() == SAIR:
            break

print('Sistema encerrado.')