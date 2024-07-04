def calculo():
    k = int(input())  # número de casos de teste
    while k != 0:  # enquanto k for diferente de 0
        n, m = map(int, input().split())  # coordenadas do ponto de divisão
        for i in range(k):  # percorre os casos de teste
            x, y = map(int, input().split())  # coordenadas do ponto
            if x == n or y == m:  # se x for igual a n ou y for igual a m
                print("divisa")  
            elif x < n and y > m:  # se x for menor que n e y for maior que m
                print("NO")
            elif x > n and y > m:  # se x for maior que n e y for maior que m
                print("NE")
            elif x > n and y < m:  # se x for maior que n e y for menor que m
                print("SE")
            elif x < n and y < m:  # se x for menor que n e y for menor que m
                print("SO")
        k = int(input())


calculo()
