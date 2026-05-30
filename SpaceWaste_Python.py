from detrito_pais import lixo_pais, DETRITOS_POR_PAIS
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

def ranques(lista_detritos):
    print('\n--- 🏆 Rankings de Detritos ---')

    # ── Ranking 1: Tamanho × Peso ──────────────────────────────────────────
    print('\n  [Ranking 1] Top 5 — Pontuação (Tamanho × Peso)')

    if not lista_detritos:
        print('  Nenhum detrito cadastrado ainda.')
    else:
        ranking_tp = sorted(
            lista_detritos,
            key=lambda d: d['tamanho'] * d['peso'],
            reverse=True
        )[:5]

        for pos, d in enumerate(ranking_tp, start=1):
            pontuacao = d['tamanho'] * d['peso']
            print(f'  {pos}º {d["nome"]:20s} — {pontuacao:>10.2f} pts'
                  f'  (tam: {d["tamanho"]} m | peso: {d["peso"]} kg)')

    # ── Ranking 2: Países ──────────────────────────────────────────────────
    print('\n  [Ranking 2] Top 5 — Países com mais lixo espacial')

    ranking_paises = sorted(
        DETRITOS_POR_PAIS.items(),
        key=lambda item: item[1]['estimativa'],
        reverse=True
    )[:5]

    for pos, (nome_pais, dados) in enumerate(ranking_paises, start=1):
        sigla  = dados['sigla']
        estim  = dados['estimativa']
        print(f'  {pos}º {nome_pais.title():25s} ({sigla}) — ~{estim:,} objetos rastreáveis')


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
                ranques(lista_detritos)
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