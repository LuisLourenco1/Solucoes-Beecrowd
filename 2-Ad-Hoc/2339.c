#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void calculo(char *texto) {
    // separando os valores lidos na primeira linha de input
    int i = 0, j = 0;
    int vet[3];
    char valor[100] = "";

    // percorrendo o texto para separar os valores
    while (texto[i] != '\0') {  // enquanto string não acabar
        if (texto[i] == ' ') { 
            // convertendo o valor lido para inteiro
            vet[j] = atoi(valor);
            strcpy(valor, "");  // limpando a string
            j++;
        } else {  // se não for espaço
            strncat(valor, &texto[i], 1);  // concatenando o valor lido
        }
        i++;
    }

    // loop termina antes de adicionar o último valor, então adicionamos aqui
    if (strlen(valor) > 0) {
        vet[j] = atoi(valor);
    }

    // atribuindo valores às variáveis
    int c = vet[0];  // número de competidores
    int p = vet[1];  // número de folhas de papel compradas
    int f = vet[2];  // número de folhas de papel para cada competidor

    char resposta[0] = "";

    resposta[0] = (c * f <= p) ? 'S' : 'N';

    printf("%c\n", resposta[0]);
}


int main() {
    char texto[100];  // primeira linha de input
    fgets(texto, 100, stdin);  // lendo a primeira linha de input
    calculo(texto);  // chama a função que faz o cálculo

    return 0;
}