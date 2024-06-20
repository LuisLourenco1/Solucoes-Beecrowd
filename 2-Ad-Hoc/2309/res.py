def calculo():
    # lendo número de partidas
    numeroPartidas = int(input())

    # array que armazenará as cartas de cada partida
    cartas = []

    # lendo as cartas de cada partida
    for i in range(numeroPartidas):
        cartas.append(list(map(int, input().split())))

    # armazenará a quantidade de vitórias de cada jogador
    adalberto = bernadete = 0

    # 4 5 6 7 Q J K A 2 3
    # 1 = A, 2 = 2, 3 = 3, 4 = 4, 5 = 5, 6 = 6, 7 = 7, 12 = Q, 11 = J, 13 = K

    # loop para organizar os valores das cartas e facilitar no cálculo depois (apenas comparar se o valor é maior ou menor)
    for i in range(numeroPartidas):
        # substituindo valores para a lógica do truco funcionar
        for j in range(6):
            if cartas[i][j] == 1:
                cartas[i][j] = 14
            elif cartas[i][j] == 2:
                cartas[i][j] = 15
            elif cartas[i][j] == 3:
                cartas[i][j] = 16
            elif cartas[i][j] == 12:
                cartas[i][j] = 11
            elif cartas[i][j] == 11:
                cartas[i][j] = 12

    # loop para calcular as vitórias de cada jogador
    for i in range(numeroPartidas):
        ada = ber = 0
        for j in range(3):
            if cartas[i][j] >= cartas[i][j + 3]:
                ada +=1
            elif cartas[i][j] < cartas[i][j + 3]:
                ber +=1

        if ada > ber:
            adalberto +=1
        else:
            bernadete +=1
        
    print(adalberto, bernadete)


calculo()
