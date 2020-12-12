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

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

GRAVIDADE = 9.81
EPSILON = 0.01
DELTA_T = 0.01
PI = 3.14159265358979323846


def seno(theta):
    """
    Esta função aproxima o valor da função seno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do seno do ângulo theta.
    """
    theta = theta * PI / 180
    serie = theta
    termo = theta
    i = 2

    while (abs(termo) > 1E-10):
        termo *= -1 * theta * theta / (i * (i + 1))
        serie += termo
        i += 2

    return serie


def cosseno(theta):
    """
    Esta função aproxima o valor da função cosseno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do cosseno do ângulo theta.
    """
    theta = theta * PI / 180
    serie = 1
    termo = 1
    i = 1

    while (abs(termo) > 1E-10):
        termo *= -1 * theta * theta / (i * (i + 1))
        serie += termo
        i += 2

    return serie


def raizQuadrada(x):
    """
    Esta função aproxima o valor da raiz quadrada de x, através da
    fórmula de recorrência r_0 = x e r_{n+1} = 1/2 (r_n+ x/r_n)
    enquanto o módulo da diferença entre os dois últimos valores
    calculados for maior que 1e-10.
    Entrada: O valor de x
    Saída: A aproximação da raiz quadrada de x.
    """
    if x == 0:
        return 0.0

    r1 = x
    r2 = 1 / 2 * (r1 + x / r1)

    while abs(r2 - r1) > 1E-10:
        r1 = r2
        r2 = 1 / 2 * (r1 + x / r1)

    return r2


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    x += vx * dt
    y += vy * dt - GRAVIDADE * dt ** 2 / 2

    return [x, y]


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    """
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    """
    vy -= GRAVIDADE * dt

    return [vx, vy]


def distanciaPontos(x1, y1, x2, y2):
    """
    Esta função calcula a distância entre dois pontos dados por
    (x1, y1) e (x2, y2).
    Entrada: As coordenadas de dois pontos no plano, x1, y1, x2, y2,
    em metros.
    Saída: A distância entre (x1, y1) e (x2, y2) em metros.
    """
    return raizQuadrada((x2 - x1) ** 2 + (y2 - y1) ** 2)


def houveColisao(x_pokebola, y_pokebola, x_pokemon, y_pokemon, r):
    """
    Esta função calcula se houve ou não colisão entre a pokebola e o
    pokemon considerando-se um raio r.
    Entrada: posição x e y da pokebola, posição x e y do pokemon
    e o raio r, todas medidas em metros.
    Saída: Retorna True caso haja colisão, e False caso contrário.
    """
    if distanciaPontos(x_pokebola, y_pokebola, x_pokemon, y_pokemon) > r:
        return False
    else:
        return True


def simula_lancamento(x_pokebola, y_pokebola,
                      v_lancamento, angulo_lancamento,
                      x_pokemon, y_pokemon, r):
    """
    Esta função simula o lançamento da bola até que ela atinja o
    pokemon, ou o solo a menos de EPSILON.
    Na simulação, considere as seguintes constantes:
    EPSILON é uma constante de precisão de 1.0e-2 metro.
    DELTAT é uma constante de precisão de 1.0e-2 segundo.
    Entrada: Posição inicial da pokebola (xpokebola e ypokebola)
    em metros.
    Posição do pokemon (xpokemon e ypokemon) em metros.
    Velocidade escalar em metros por segundo
    e ângulo de lançamento em graus.
    O raio r em metros.
    Saída: Três valores: Um booleano (True se o lançamento teve sucesso
    e acertou o pokemon, ou False caso contrário) e as coordenadas finais
    x e y da pokébola.
    """
    continuar = True
    vx = v_lancamento * cosseno(angulo_lancamento)
    vy = v_lancamento * seno(angulo_lancamento)

    while continuar:
        x_pokebola = atualizaPosicao(x_pokebola, y_pokebola, vx, vy)[0]
        y_pokebola = atualizaPosicao(x_pokebola, y_pokebola, vx, vy)[1]
        vx = atualizaVelocidade(vx, vy)[0]
        vy = atualizaVelocidade(vx, vy)[1]

        capturado = houveColisao(x_pokebola, y_pokebola, x_pokemon, y_pokemon, r)

        if y_pokebola < EPSILON or capturado:
            continuar = False

    # return distanciaPontos(x_pokebola, y_pokebola, x_pokemon, y_pokemon) - r
    return capturado, x_pokebola, y_pokebola


def main():
    x_pokemon = int(input("Digite a coordenada x do pokemon: "))
    y_pokemon = int(input("Digite a coordenada y do pokemon: "))
    r = float(input("Digite o raio do pokemon (> 0) em metros: "))

    capturado = False
    pokebolas = 3
    tentativa = 1

    while (not capturado and pokebolas):
        print()
        print(f"Tentativa {tentativa}")
        x_pokebola = int(input("\tDigite a coordenada x do treinador: "))
        y_pokebola = int(input("\tDigite a coordenada y do treinador: "))
        v_lancamento = int(input("\tDigite a velocidade do lancamento em m/s: "))
        angulo_lancamento = int(input("\tDigite o angulo de lancamento em graus: "))
        print()

        distancia = simula_lancamento(x_pokebola, y_pokebola, v_lancamento, angulo_lancamento, x_pokemon, y_pokemon, r)
        if distancia <= r:
            capturado = True

        if capturado:
            print("A pokebola atingiu o pokemon")
        else:
            print(f"A pokebola nao atingiu o pokemon por {distancia} metros")

        tentativa += 1
        pokebolas -= 1


# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================


# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN
# ======================================================================
