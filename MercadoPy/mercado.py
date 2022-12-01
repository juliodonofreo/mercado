from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def validar_menu() -> int:
    while True:
        try:
            opcao = int(input('\n'))
        except ValueError:
            print('a opção deve ser um número, por favor digite novamente: ', end='')
        else:
            if opcao < 1 or opcao > 6:
                print('Opção inválida. ')
            else:
                return opcao


def validar_codigo(texto='', /):
    while True:
        lista_codigos = [produto.codigo for produto in produtos]
        try:
            codigo = int(input(texto))
        except ValueError:
            print('o código deve ser um número inteiro. ', end='')
        else:
            if codigo not in lista_codigos and codigo != 0:
                print('o código deve ser um dos mencionados ou 0. ', end='')
            else:
                return codigo


def menu() -> None:
    print('=' * 25)
    print(f"{'=' * 5} Bem vindo(a) {'=' * 5}")
    print(f'{"=" * 5} projeto loja {"=" * 5}')
    print('=' * 25)
    print('Selecione uma opção abaixo: ')
    print('1 - cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - fechar pedido')
    print('6 - sair')
    opcao: int = validar_menu()

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedidos()
    else:
        print('Volte sempre. ')
        sleep(2)
        exit()


def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('=' * 20)

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    print(f'O produto {produto.nome} foi cadastrado com sucesso. ')
    produtos.append(produto)
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) == 0:
        print('Ainda não há produtos cadastrados. ')
    else:
        print('Listagem de produtos')
        print('=' * 20)
        for produto in produtos:
            print(produto)
            print('-' * 10)
            sleep(1)
    sleep(2)
    menu()


def comprar_produto() -> None:
    if not produtos:
        print('ainda não existem produtos para vender. ')
        sleep(2)
        menu()
    else:
        print('Informe o código do produto que deseja adicionar ao carrinho [0 cancela]: ')
        print("-------------------------------------------------------------")
        print('=================== Produtos Disponíveis =====================')
        for produto in produtos:
            print(produto)
            print('-----------------------------------------------------------')
            sleep(1)
        codigo: int = validar_codigo()
        produto: Produto = pega_produto_por_codigo(codigo)
        if codigo == 0:
            sleep(2)
            menu()
        else:
            if carrinho:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho. ')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                    if not tem_no_carrinho:
                        prod = {produto: 1}
                        carrinho.append(prod)
                        print(f'O produto {produto.nome} foi adicionado ao carrinho. ')
                        sleep(2)
                        menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'o produto {produto.nome} foi adicionado ao carrinho. ')
                sleep(2)
                menu()
    sleep(2)


def visualizar_carrinho() -> None:
    if not carrinho:
        print('ainda não existem produtos no carrinho. ')
    else:
        print('produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'quantidade: {dados[1]}')
                print('========================')
                sleep(1)
    sleep(2)
    menu()


def fechar_pedidos() -> None:
    if not carrinho:
        print('ainda não existem produtos no carrinho')
        menu()
    else:
        valor_total: float = 0

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('=' * 18)

        print(f'sua fatura é {formata_float_str_moeda(valor_total)}')
        print('volte sempre. ')
        carrinho.clear()
        sleep(2)


def pega_produto_por_codigo(codigo: int, /) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
