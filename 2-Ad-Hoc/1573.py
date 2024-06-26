from math import floor

def calculo():
    valores = []  # Lista para armazenar os valores de entrada
    output = []  # Lista para armazenar os valores de saída
    valores.append(list(map(int, input().split())))  # Adicionando o primeiro valor de entrada

    # Enquanto o último valor de entrada não for [0, 0, 0], adicione o valor de saída na lista de saída
    while valores[-1] != [0, 0, 0]:
        output.append(floor((valores[-1][0] * valores[-1][1] * valores[-1][2]) ** (1/3)))
        valores.append(list(map(int, input().split())))

    # Imprimindo os valores de saída
    for i in range(len(output)):
        print(output[i])


calculo()
