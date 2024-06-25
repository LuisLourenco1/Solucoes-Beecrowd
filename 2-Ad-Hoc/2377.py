def calculo():
    l, d = map(int, input().split())  # comprimento da estrada e distancia entre os pedágios
    k, p = map(int, input().split())  # custo por quilômetro percorrido e valor de cada pedágio

    # Calculando custo total da viagem
    custo_total = (l // d) * p + l * k

    print(custo_total)


calculo()