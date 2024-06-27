def probabilidade(vals):
    ev1, ev2, at, d = vals

    if ev1 == ev2 == at == d == 0:
        return None

    # Gambler's Ruin
    # Transformando as energias vitais em número de turnos necessários
    c, ev1_turns = ev1, 0
    while c > 0:
        c -= d
        ev1_turns += 1

    c, ev2_turns = ev2, 0
    while c > 0:
        c -= d
        ev2_turns += 1

    # Calculando a probabilidade de vitória do Vampiro 1
    if at == 3:
        probabilidadev1 = ev1_turns / (ev1_turns + ev2_turns)
    else:
        p = at / 6
        q = 1 - p
        qp = q / p
        probabilidadev1 = (1 - qp ** ev1_turns) / (1 - qp ** (ev1_turns + ev2_turns))

    return '{:.1f}'.format(probabilidadev1 * 100)

def calculo():
    valores = []  # Lista para armazenar os valores de entrada
    output = []  # Lista para armazenar os valores de saída

    while True:
        entrada = list(map(int, input().split()))
        if entrada == [0, 0, 0, 0]:
            break
        valores.append(entrada)

    for vals in valores:
        resultado = probabilidade(vals)
        if resultado is not None:
            output.append(resultado)

    # Imprimindo os valores de saída
    for resultado in output:
        print(resultado)

calculo()
