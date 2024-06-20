#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void calculo(char *texto) {
    // separando os valores lidos na primeira linha de input
    int i = 0, c = 0;
    int vet[4];
    char valor[100] = "";

    // percorrendo o texto para separar os valores
    while (texto[i] != '\0') {  // enquanto string não acabar
        if (texto[i] == ' ') { 
            // convertendo o valor lido para inteiro
            vet[c] = atoi(valor);
            strcpy(valor, "");  // limpando a string
            c++;
        } else {  // se não for espaço
            strncat(valor, &texto[i], 1);  // concatenando o valor lido
        }
        i++;
    }

    // loop termina antes de adicionar o último valor, então adicionamos aqui
    if (strlen(valor) > 0) {
        vet[c] = atoi(valor);
    }

    // atribuindo valores às variáveis
    int n = vet[0];  // número de instruções
    int k = vet[1];  // distância máxima
    int x = vet[2];  // posição x do evento
    int y = vet[3];  // posição y do evento

    // lendo as instruções
    char instrucoes[n];

    for (int j = 0; j < n; j++) {
        scanf(" %c", &instrucoes[j]);
        instrucoes[j] = toupper(instrucoes[j]);  // transformando em maiúscula
    }

    int suposto_x = 0, suposto_y = 0;  // posição suposta do evento que será calculada

    // verificar se a distância inicial já não é maior que a distância máxima
    float distancia = sqrt(pow(x, 2) + pow(y, 2));

    if (distancia > k) {
        printf("Trap 1\n");
        return;
    }

    for (int z = 0; z < n; z++) {
        if (instrucoes[z] == 'C') {
            suposto_x += 1;
        } else if (instrucoes[z] == 'B') {
            suposto_y -= 1;
        } else if (instrucoes[z] == 'E') {
            suposto_x -= 1;
        } else if (instrucoes[z] == 'D') {
            suposto_y += 1;
        }

        // recalculando a distância
        distancia = sqrt(pow(suposto_x - x, 2) + pow(suposto_y - y, 2));

        if (suposto_x == x && suposto_y == y) {
            printf("Sucesso\n");
            return;
        } else if (distancia > k || z == n - 1) {
            printf("Trap %d\n", z + 1);
            return;
        }
    }
}


int main() {
    char texto[100];  // primeira linha de input
    fgets(texto, 100, stdin);  // lendo a primeira linha de input
    calculo(texto);  // chama a função que faz o cálculo

    return 0;
}
