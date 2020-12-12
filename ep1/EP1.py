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

# Menssagens:
mAcertou   = '\nA pokebola atingiu o pokemon.'
mNacertou  = '\nA pokebola nao atingiu o pokemon.'
mStatus    = '> t= \t{}\tvy=\t{}\tx=\t{}\ty=\t{}'

# Dados de entrada
pokebolas = int(input(' Digite o numero N de pokebolas: '))
gravidade = int(input('Digite o valor da gravidade: '))
pcoord_x  = int(input('Digite a coordenada x (inteiro >= 0) do pokemon: '))
pcoord_y  = int(input('Digite a coordenada y (inteiro >= 0) do pokemon: '))

# Constantes:
dT = 1

acertou = False # Variavel pra definir o break na condição de ter acertado o pokemon
tentativa = 1 # variavel a ser incrementada em cada tentativa, pra fazer o print do valor

while pokebolas > 0 and acertou == False:
    print('\nTentativa {}:\n'.format(tentativa))
    
    # Entrada de posição do treinador e da velociade de lancamento:
    tcoord_x = int(input('Digite a coordenada x (inteiro >= 0) do treinador: '))
    tcoord_y = int(input('Digite a coordenada y (inteiro >= 0) do treinador: '))
    ycomp    = int(input('Digite a componente y da velocidade de lancamento: '))

    bcoord_x = tcoord_x
    bcoord_y = tcoord_y


    t = 0
    # Condiçoes pra parar a loop: XBy ser menor que 0 ou XBx passar de XPx
    while (bcoord_x <= pcoord_x) and (bcoord_y >= 0):
      print(mStatus.format(t, ycomp, bcoord_x, bcoord_y))

      prev_by = bcoord_y # Criar um backup da posição Y pra 

      # Caso tenha acertado o pokemon, imprime a mensage de aviso
      # e altera o variavel acetou pra quebrar o break do while em que esse
      # esta contido
      if bcoord_x == pcoord_x and bcoord_y == pcoord_y:
        print(mAcertou)
        acertou = True
        break
      
      # Calculo para atualizar os valores
      bcoord_y = int(bcoord_y + ycomp * dT - gravidade/2 * dT**2)
      ycomp = ycomp - gravidade * dT
      bcoord_x = bcoord_x + 1 * dT

      t += 1 # Incrementa o tempo

    # Caso seja um valor negativo imprime a ultima linha
    # Pra não imprimir um valor negativo endo que o ultimo valor ja foi 0
    # usa o backup da posicao Y para compara e ver se imprime o numro negativo ou não
    if (bcoord_y < 0 and prev_by != 0 and bcoord_x <= pcoord_x):
        print(mStatus.format(t, ycomp, bcoord_x, bcoord_y))


    # Condiçoes pra garantir que esta imprimindo a menssagem de não acertou
    # XB ser diferente de XP e idem para eixo Y 
    if (bcoord_x != pcoord_x and bcoord_y != pcoord_y) or (bcoord_y < 0 and prev_by != 0 and bcoord_x <= pcoord_x):
      print(mNacertou)
      #print(" ")

    tentativa += 1 # Incrementa tentativa
    pokebolas -= 1 # Decrementa pokebolas