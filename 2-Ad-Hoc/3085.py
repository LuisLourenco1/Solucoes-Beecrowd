def calculo(first):
    # separando os valores
    valores = first.split()  # separando os valores por espaço entre eles
    
    # atribuindo os valores às variáveis e convertendo-os para inteiro
    n = int(valores[0])  # número de instruções
    k = int(valores[1])  # distância máxima
    x = int(valores[2])  # posição x do evento
    y = int(valores[3])  # posição y do evento

    instrucoes = []  # lista que vai receber as instruções
    # C, B, E, D: Cima, baixo, esquerda, direita

    for i in range(n):
        instrucoes.append(str(input()).upper())

    distancia = (x**2 + y**2)**0.5  # calculando distância euclidiana do ponto inicial ao ponto do evento

    suposto_x = 0  # variável que gradativamente vai receber a posição x conforme as instruções
    suposto_y = 0  # variável que gradativamente vai receber a posição y conforme as instruções

    # primeiro passo: verificar se já é uma farsa no início, caso a distância euclidiana seja maior que a distância máxima
    if distancia > k:
        print('Trap 1')
        return
    
    # segundo passo: verificar instrução a instrução se a distância uma hora passará do limite k
    for i in range(n):
        if instrucoes[i] == 'C':
            suposto_y += 1
        elif instrucoes[i] == 'B':
            suposto_y -= 1
        elif instrucoes[i] == 'E':
            suposto_x -= 1
        elif instrucoes[i] == 'D':
            suposto_x += 1

        # recalculando a distância euclidiana
        distancia = ((suposto_x - x)**2 + (suposto_y - y)**2)**0.5

        # se chegar na posição do evento, sucesso
        if suposto_x == x and suposto_y == y:
            print('Sucesso')
            return
        elif distancia > k or i == n-1:  # se a distância passar do limite k ou se for a última instrução, farsa
            print(f'Trap {i+1}')
            return
    

texto = str(input())  # primeira linha de input, vai receber os 4 valores
calculo(texto)
