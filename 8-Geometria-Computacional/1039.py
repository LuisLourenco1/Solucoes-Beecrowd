import sys
import math


# Função que verifica se o círculo 2 está dentro do círculo 1
def circulo_dentro(R1, X1, Y1, R2, X2, Y2):
    distancia = math.sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)  # Calcula a distância entre os centros dos círculos
    return distancia + R2 <= R1  # Retorna True se a distância entre os centros mais o raio do círculo 2 for menor ou igual ao raio do círculo 1


def calculo():
    for line in sys.stdin:  # Para cada linha da entrada padrão
        data = list(map(int, line.split()))  # Transforma a linha em uma lista de inteiros
        R1, X1, Y1, R2, X2, Y2 = data  # Desempacota a lista de inteiros
        if circulo_dentro(R1, X1, Y1, R2, X2, Y2):  # Se o círculo 2 está dentro do círculo 1
            print('RICO')  # Imprime 'RICO'
        else:  # Se o círculo 2 não está dentro do círculo 1
            print('MORTO')  # Imprime 'MORTO'


calculo()
