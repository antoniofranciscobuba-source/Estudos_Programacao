#include <stdio.h>
int adicao(int a, int b) {
    return a + b;
}

int main(void) {

    int a;
    int b;
    int soma;
   
    printf("Insira o primerio numero: ");
    scanf("%d", &a);
    printf("Insira o segundo numero: ");
    scanf("%d", &b);

    soma = adicao(a, b);

    printf("A soma entre %d e %d e igual a %d\n", a, b, soma);
    return 0;
}