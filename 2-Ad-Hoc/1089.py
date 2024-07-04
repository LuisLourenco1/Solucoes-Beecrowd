def calculo():
    n = int(input())  # número de samples
    while n != 0:
        samples = list(map(int, input().split()))  # samples
        samples.append(samples[0])  # adiciona o primeiro elemento no final
        samples.insert(0, samples[-2])  # adiciona o penúltimo elemento no início (que é o último elemento)
        peaks = 0  # número de picos
        for i in range(1, n+1):  # percorre os samples
            if samples[i] > samples[i-1] and samples[i] > samples[i+1]:  # verifica se é um pico
                peaks += 1
            elif samples[i] < samples[i-1] and samples[i] < samples[i+1]:  # verifica se é um vale
                peaks += 1
        print(peaks)  # imprime o número de picos
        n = int(input())  # número de samples

    
calculo()
