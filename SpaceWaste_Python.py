from detrito_pais import lixo_pais, DETRITOS_POR_PAIS

import time

# ============================================================
# FUNÇÕES DE VALIDAÇÃO
# ============================================================

def validar_email(email):
    """
    Valida se o email possui '@' e '.'.
    Parâmetro: email (str) — email digitado pelo usuário.
    Retorno: bool — True se válido, False caso contrário.
    """
    return '@' in email and '.' in email


def validar_numero_positivo(prompt):
    """
    Solicita um número positivo ao usuário, repetindo até receber entrada válida.
    Parâmetro: prompt (str) — mensagem exibida ao usuário.
    Retorno: float — número positivo informado.
    """
    while True:
        try:
            valor = float(input(prompt))
            if valor <= 0:
                print('  ⚠ O valor deve ser maior que zero. Tente novamente.')
            else:
                return valor
        except ValueError:
            print('  ⚠ Entrada inválida. Digite um número.')


# ============================================================
# ENTRADA / LOGIN
# ============================================================

def entrada():
    """
    Realiza o login do usuário solicitando nome e email.
    Sem parâmetros.
    Retorno: dict — dicionário com 'nome' e 'email' do usuário.
    """
    print('\nOlá! Seja bem-vindo ao SpaceWaste 🚀')
    print('Informe suas credenciais para continuar.\n')

    nome = input('Informe seu nome: ').strip()
    while not nome:
        print('  ⚠ Para continuar, informe seu nome.')
        nome = input('Informe seu nome: ').strip()

    while True:
        email = input('Informe seu email: ').strip()
        if validar_email(email):
            break
        print('  ⚠ Email inválido. Verifique se possui "@" e ".".')

    print(f'\nLogin finalizado! Seja bem-vindo ao SpaceWaste, {nome}! 🌌')

    usuario = {
        'nome': nome,
        'email': email,
    }
    return usuario


# ============================================================
# MENU PRINCIPAL
# ============================================================

def pagina_inicial():
    """
    Exibe o menu principal e retorna a opção escolhida.
    Sem parâmetros.
    Retorno: str — opção digitada pelo usuário.
    """
    print('\n' + '=' * 40)
    print('         🛸  S P A C E W A S T E  🛸')
    print('=' * 40)
    print('  1 - Cadastrar detrito espacial')
    print('  2 - Simulação de reentrada atmosférica')
    print('  3 - Relatório de detritos cadastrados')
    print('  4 - Ranking de detritos e países')
    print('  5 - Lixo espacial por país')
    print('  6 - Sobre o SpaceWaste')
    print('  7 - Sair do aplicativo')
    print('=' * 40)
    return input('  Ação desejada: ').strip()


# ============================================================
# OPÇÃO 1 — CADASTRO DE DETRITO
# ============================================================

def cadastro_detrito(lista_detritos):
    """
    Permite ao usuário cadastrar um detrito espacial fictício.
    Parâmetro: lista_detritos (list) — lista onde o detrito será adicionado.
    Sem retorno — modifica a lista diretamente.
    """
    print('\n--- Cadastro de Detrito Espacial ---')
    print('Aqui você pode criar seu próprio lixo espacial.\n')

    dnome = input('  Nome do detrito: ').strip()
    while not dnome:
        print('  ⚠ O nome não pode ser vazio.')
        dnome = input('  Nome do detrito: ').strip()

    dtamanho = validar_numero_positivo('  Tamanho do detrito em metros: ')
    dpeso    = validar_numero_positivo('  Peso do detrito em quilos: ')
    dalt     = validar_numero_positivo('  Altitude do detrito na atmosfera em km: ')

    detrito = {
        'nome':     dnome,
        'tamanho':  dtamanho,
        'peso':     dpeso,
        'altitude': dalt,
    }
    lista_detritos.append(detrito)
    print(f'\n  ✅ Detrito "{dnome}" cadastrado com sucesso!')


# ============================================================
# OPÇÃO 2 — SIMULAÇÃO DE REENTRADA
# ============================================================

def tempo_reentrada(dalt):
    """
    Estima o tempo de reentrada com base na altitude.
    Parâmetro: dalt (float) — altitude em quilômetros.
    Retorno: str — estimativa textual do tempo de reentrada.
    """
    if dalt < 300:
        return 'menos de 1 ano'
    elif dalt < 400:
        return 'alguns anos'
    elif dalt < 600:
        return 'décadas'
    elif dalt < 1000:
        return 'séculos'
    else:
        return 'milênios (praticamente permanente)'


def simulacao(lista_detritos):
    """
    Simula a reentrada atmosférica de todos os detritos cadastrados.
    Parâmetro: lista_detritos (list) — lista de detritos cadastrados.
    Sem retorno — exibe a simulação no terminal.
    """
    if not lista_detritos:
        print('\n  ⚠ Nenhum detrito cadastrado. Vá à opção 1 primeiro.')
        return

    print('\n--- Simulação de Reentrada Atmosférica ---')
    for d in lista_detritos:
        print(f'\n  🔥 Simulando: {d["nome"]}')

        if d['peso'] < 10:
            resultado = 'Incinerado completamente na atmosfera'
        elif d['tamanho'] < 0.5:
            resultado = 'Fragmentado e incinerado'
        elif d['peso'] > 1000:
            resultado = 'Impacto no solo'
        else:
            resultado = 'Fragmentos pequenos caíram no oceano'

        tempo = tempo_reentrada(d['altitude'])

        etapas = [
            (d['altitude'],       'Detrito em órbita estável...'),
            (d['altitude'] * 0.6, 'Começando a perder altitude...'),
            (120,                 'Entrando na termosfera — fricção intensa!'),
            (80,                  'Temperatura ultrapassando 1600°C!'),
            (50,                  'Ablação em andamento...'),
            (0,                   resultado),
        ]

        for alt, msg in etapas:
            print(f'  [{alt:.0f} km] {msg}')
            time.sleep(0.8)

        print(f'\n  ─────────────────────────────────')
        print(f'  Altitude inicial  : {d["altitude"]} km')
        print(f'  Tempo de reentrada: {tempo}')
        print(f'  Resultado         : {resultado}')
        print(f'  ─────────────────────────────────')


# ============================================================
# OPÇÃO 3 — RELATÓRIO
# ============================================================

def relatorio(lista_detritos):
    """
    Exibe o relatório completo de todos os detritos cadastrados.
    Parâmetro: lista_detritos (list) — lista de detritos cadastrados.
    Sem retorno — imprime o relatório no terminal.
    """
    print('\n--- Relatório de Detritos Cadastrados ---')

    if not lista_detritos:
        print('  Nenhum detrito cadastrado ainda.')
        return

    print(f'  Total de detritos: {len(lista_detritos)}\n')
    for i, d in enumerate(lista_detritos, start=1):
        print(f'  [{i}] {d["nome"]}')
        print(f'      Tamanho : {d["tamanho"]} m')
        print(f'      Peso    : {d["peso"]} kg')
        print(f'      Altitude: {d["altitude"]} km')
        print()


# ============================================================
# OPÇÃO 4 — RANKING
# ============================================================

def ranques(lista_detritos):
    """
    Exibe dois rankings: Top 5 detritos por pontuação (tamanho × peso)
    e Top 5 países com mais lixo espacial.
    Parâmetro: lista_detritos (list) — lista de detritos cadastrados.
    Sem retorno — imprime os rankings no terminal.
    """
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
        sigla = dados['sigla']
        estim = dados['estimativa']
        print(f'  {pos}º {nome_pais.title():25s} ({sigla}) — ~{estim:,} objetos rastreáveis')


# ============================================================
# OPÇÃO 6 — SOBRE O SPACEWASTE
# ============================================================

def sobre():
    """
    Exibe uma breve descrição textual do projeto SpaceWaste.
    Sem parâmetros nem retorno.
    """
    print('\n--- Sobre o SpaceWaste ---')
    print('  O SpaceWaste é um simulador de lixo espacial desenvolvido em Python.')
    print('  O sistema permite cadastrar detritos fictícios, simular sua reentrada')
    print('  na atmosfera terrestre e visualizar rankings e estatísticas por país.')
    print('  O projeto aborda a problemática real dos detritos orbitais, que hoje')
    print('  somam mais de 27.000 objetos rastreáveis em órbita ao redor da Terra.')


# ============================================================
# EXECUÇÃO DO APP
# ============================================================

def executar_app(usuario):
    """
    Controla o loop principal do aplicativo, chamando as funções do menu.
    Parâmetro: usuario (dict) — dicionário com nome e email do usuário logado.
    Sem retorno.
    """
    nome = usuario['nome']
    lista_detritos = []

    while True:
        escolha = pagina_inicial()

        match escolha:
            case '1':
                cadastro_detrito(lista_detritos)
            case '2':
                simulacao(lista_detritos)
            case '3':
                relatorio(lista_detritos)
            case '4':
                ranques(lista_detritos)
            case '5':
                lixo_pais()
            case '6':
                sobre()
            case '7':
                print(f'\n  Até mais, {nome}! 👋')
                break
            case _:
                print('\n  ⚠ Opção inválida! Escolha entre 1 e 7.')


# ============================================================
# MAIN
# ============================================================

def main():
    """Ponto de entrada do programa."""
    usuario = entrada()
    executar_app(usuario)

main()