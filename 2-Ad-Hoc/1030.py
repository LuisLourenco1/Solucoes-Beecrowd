def calculo():
    nc = int(input())  # número de casos de teste

    for i in range(nc):
        n, k = map(int, input().split())  # n = número de pessoas, k = salto
        lista = [x for x in range(1, n + 1)]  # lista de pessoas
        marcador = 0

        # enquanto houver mais de uma pessoa na lista
        while len(lista) > 1:
            marcador = (marcador + k - 1) % len(lista)  # calcula a posição da pessoa a ser eliminada
            lista.pop(marcador)  # elimina a pessoa
            
        print(f'Case {i + 1}: {lista[0]}')

calculo()
