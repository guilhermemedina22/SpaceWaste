from detrito_pais import lixo_pais
##funções de validação

def validar_email(email):
    return '@' in email and '.' in email


##entrada de valores
def entrada():
    print('\nolá seja bem vindo ao SpaceWaste')
    print('informe suas credencias para continuar.\n')

    nome = input('informe seu nome: ').strip()
    while not nome:
        print('para continuar informe seu nome')
        nome = input('informe seu nome: ').strip()

    while True:
        email = input('informe seu email: ') .strip()
        if validar_email(email):
            break
        print('Email invalido, veerifique se ele possui @ ou . ')

    print(f'login finalizado, seja bem vindo ao SpaceWaste {nome}')

    usuario = {
        'nome': nome,
        'email': email,
    }
    return usuario



def pagina_inicial():
    print('\n\n=====SpaceWaste=====')
    print('1 - cadastro de detrito ficticio')
    print('2 - simulação de reentrada na atmosfera')
    print('3 - Relatório estatistico')
    print('4 - ranque de detritos')
    print('5 - Lixo espacial no país __')
    print('6 - sair do aplicativo')
    return input('ação desejada: ').strip()
## opções do menu

def cadastro_detrito(lista_detritos):
    print('aqui você pode criar seu próprio lixo espacial')
    dnome = input('nome do detrito: ')
    dtamanho = float(input('tamanho do detrito em metros: '))
    dpeso = float(input('peso do detrito em quilos: '))
    dalt = float(input('altitude do detrito na atimosfera em quilometros: '))

    detrito = {
        'nome': dnome,
        'tamanho': dtamanho,
        'peso': dpeso,
        'altitude': dalt,
    }
    lista_detritos.append(detrito)
    
def simulacao():
    print('em desenvolvimento')

def relatorio(lista_detritos):
    print('\n--- Relatório de Detritos ---')

    if not lista_detritos:
        print('Nenhum detrito cadastrado ainda.')
        return

    for i, d in enumerate(lista_detritos, start=1):
        print(f'\n  [{i}] {d["nome"]}')
        print(f'      Tamanho : {d["tamanho"]} m')
        print(f'      Peso    : {d["peso"]} kg')
        print(f'      Altitude: {d["altitude"]} km')
def ranques():
    print('em desenvolvimento')   



def executar_app(usuario):
    nome = usuario['nome']
    lista_detritos = []

    while True:
        escolha = pagina_inicial()
        
        match escolha:
            case '1':
                cadastro_detrito(lista_detritos)
            case '2':
                simulacao()
            case '3':
                relatorio(lista_detritos)
            case '4':
                ranques()
            case '5':
                lixo_pais()
            case '6':
                print(f'até mais {nome}')
                break
            case _:
                print('\n    ⚠ Opção inválida! Escolha entre 1 e 6.')

def main():
    usuario = entrada()
    executar_app(usuario)

main()