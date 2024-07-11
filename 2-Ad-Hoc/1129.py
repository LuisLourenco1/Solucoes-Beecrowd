def calculo():
    n = int(input())  # número de testes
    while n != 0:  # enquanto n for diferente de 0
        for i in range(n):  # para cada teste
            a, b, c, d, e = map(int, input().split())  # lê os valores
            valores = [a, b, c, d, e]  # coloca os valores em uma lista
            count = 0  # contador
            pos = 0  # posição

            for i in range(5):  # para cada valor
                if valores[i] <= 127:  # se o valor for menor ou igual a 127 (marcado)
                    count += 1  # incrementa o contador
                    pos = i  # guarda a posição
                
            if count == 1:  # se o contador for igual a 1 (somente uma alternativa marcada)
                print(chr(65 + pos))  # imprime a letra correspondente
            else:  # se não (mais de uma alternativa marcada ou nenhuma)
                print('*')  # imprime '*'
        n = int(input())  # lê o próximo n (número de testes)


calculo()