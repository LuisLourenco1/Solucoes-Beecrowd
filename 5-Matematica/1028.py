# Função recursiva para calcular o MDC
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def calculo():
    n = int(input())
    valores = []  # Lista para armazenar os valores de entrada
    output = []  # Lista para armazenar os valores de saída

    for i in range(n):
        valores.append(list(map(int, input().split())))  # Guardando os valores lidos
        output.append(mdc(valores[i][0], valores[i][1]))  # Calculando o MDC e guardando na lista de saída

    for i in range(n):
        print(output[i])


calculo()
