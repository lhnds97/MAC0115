"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Lucas Hernandes da Costa Porto
  NUSP : 11918140
  Turma: 224
  Prof.: Hirata

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

import math

DELTA_T = 0.1
GRAVIDADE = 2


# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP3.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

def leArquivo(nomeArquivo='entrada.txt'):
    """
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    Entrada: arquivo cujo nome está armazenado em nomeArquivo.
             Por default, é 'entrada.txt'
    Saída: uma lista de listas, onde o primeiro elemento é uma
           lista de inteiros [m, n] (dimensões da matriz) e os
           elementos subsequentes são listas que representam as
           característica lidas dos Pokémons na forma:
                [nome, raio, x, y]
    """

    arquivo = open(nomeArquivo, 'r').readlines()
    matriz = []

    for item in arquivo:
        matriz.append(item.split())

    # Converter para numerico
    matriz[0][0] = int(matriz[0][0])
    matriz[0][1] = int(matriz[0][1])

    for i in range(1, len(matriz)):
        matriz[i][1] = int(matriz[i][1])
        matriz[i][2] = int(matriz[i][2])
        matriz[i][3] = int(matriz[i][3])

    return matriz


def criaMatriz(m, n):
    """
    Esta função cria e retorna uma lista de listas.
    Entrada: dois inteiros que representam o número de linhas e
             o número de colunas da matriz.
    Saída: uma lista de m listas, cada uma com n elementos, todos
           inicializados com zeros.
    """

    # Para cada elemento entre 0 e m cria uma linha para diconar na matriz
    # e para cada elemento entre 0 e n adiciona um item na linha
    matriz = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append('0')
        matriz.append(row)

    return matriz


def populaMatriz(matriz, pokemons):
    """
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    Entrada: matriz representada por uma lista de listas
    Saída: A matriz fornecida é modificada.
    """

    i = 1  # id do pokemon

    for pokemon in pokemons:
        matriz = preenchePokemon(matriz,
                                 i,
                                 pokemon[2],
                                 -pokemon[3] - 1,  # O chao fica como referecial para o index x
                                 pokemon[1])
        i += 1

    return matriz


def preenchePokemon(matriz, id, x, y, raio):
    """
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)
    Entrada: matriz representada por uma lista de listas
             id é o número a preencher a matriz; para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente.
             x,y são as coordenadas do ponto central
             raio é a distância a ser guardada a partir do
             ponto central.
    Saída: A matriz fornecida é modificada.
    """
    for i in range(y - raio, y + raio + 1):
        for j in range(x - raio, x + raio + 1):
            matriz[i][j] = id

    return matriz


def removePokemon(matriz, id, pokemons):
    """
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    Entrada: matriz representada por uma lista de listas;
             id é o número a preencher a matriz, para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente;
             pokemons lista contendo as listas que representam pokémons.
    Saída: A matriz fornecida é modificada.
    """
    id = int(id)

    y = -pokemons[id][3]-1  # O chao fica como referecial para o index x
    x = pokemons[id][2]
    raio = pokemons[id][1]

    for i in range(y - raio, y + raio + 1):
        for j in range(x - raio, x + raio + 1):
            matriz[i][j] = '0'

    return matriz


def imprimeMatriz(matriz):
    """
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical,
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    """
    m = len(matriz)
    n = len(matriz[0])

    for i in range(m):
        for j in range(n):
            # Para facilitar a visualizacao trocar o '0' por '.'
            if matriz[i][j] == '0':
                imprimir = '.'
            else:
                imprimir = matriz[i][j]

            print(imprimir, end="")
        print()
    print()

    return None


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    """
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    """
    x_att = x + vx * dt
    y_att = y + vy * dt + GRAVIDADE / 2 * dt * dt

    return x_att, y_att


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    """
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    """
    vy_att = vy + GRAVIDADE * dt
    vx_att = vx

    return vx_att, vy_att


def grau2Radiano(theta):
    """
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    """
    return theta * math.pi / 180


def main():
    nome = input("Digite o nome do arquivo: ")
    N = int(input("Digite o numero N de pokebolas: "))

    lista = leArquivo(nomeArquivo=nome)
    m, n = lista[0]

    pokemons = lista[1:]

    matriz = criaMatriz(m, n)
    matriz = populaMatriz(matriz, pokemons)

    pokemonsLivres = len(pokemons)
    capturado = False
    abscissaCaptura = 0  # chao

    while (N > 0 and pokemonsLivres > 0):
        if not capturado:
            x = int(input("Digite a coordenada x do treinador: "))
        else:
            x = abscissaCaptura

        y = m - 1
        capturado = False

        print(f'pokebolas disponiveis = {N}')
        matriz[y][x] = 'T'

        print("Estado atual do jogo:")
        imprimeMatriz(matriz)

        matriz_lancamento = list(map(list, matriz))
        matriz[y][x] = '0'

        v = int(input("Digite a velocidade de lancamento em m/s: "))

        theta = int(input("Digite o angulo de lancamento em graus: "))
        theta = grau2Radiano(theta)

        vx = math.cos(theta) * v
        vy = -math.sin(theta) * v

        while (not capturado and (x >= 0 and x <= n - 1) and (y <= m - 1)):
            if (round(y) >= 0 and round(x) >= 0):
                # Caso tenha atingido a area em que esta o pokemon
                # que qualquer m[x][y] != (T ou 0) atualiza a variavel `capturado`
                if matriz[round(y)][round(x)] != '0' and matriz[round(y)][round(x)] != 'T':
                    capturado = True
                    pokemonCapturado = matriz[round(y)][round(x)] - 1 # o id dos pokemons inicia em 1
                    abscissaCaptura = round(x)

                # Caso nao tenha atingido um pokemon altera o caracter da
                # posicao com o `o`
                if matriz_lancamento[round(y)][round(x)] != 'T':
                    matriz_lancamento[round(y)][round(x)] = "o"

            x, y = atualizaPosicao(x, y, vx, vy)
            vx, vy = atualizaVelocidade(vx, vy)

        N -= 1

        print("Representacao grafica do lancamento: ")
        imprimeMatriz(matriz_lancamento)

        # Se o a variavel cpturado for True, o pokemnon foi
        # atingido, entao remove ele da matriz e decrementa o
        # numero de pokemons livres
        if capturado:
            matriz = removePokemon(matriz, pokemonCapturado, pokemons)
            print(f'Um {pokemons[int(pokemonCapturado)][0]} foi capturado!\n')
            pokemonsLivres -= 1
        else:
            print('O lancamento nao capturou pokemon algum\n')

    # mensagens para caso nao existam mais pokemon ou pokebolas
    if pokemonsLivres == 0:
        print('Parabens! Todos pokemons foram capturados')
    elif N == 0:
        print('Jogo encerrado')


main()
