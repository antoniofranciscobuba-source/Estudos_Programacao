#include <stdio.h>

int main() {
    int a, b, soma, sub, mult, divi;

    printf("Digite o primeiro valor: ");
    scanf("\n%d", &a);
    printf("Digite o segundo valor: ");
    scanf("\n%d", &b);

    soma = a + b;
    sub = a - b;
    mult = a * b;
    divi = a / b;

    printf("Resultados:\n");
    printf("soma: %d.\n", soma);
    printf("subitra.: %d.\n", sub);
    printf("Multipli.: %d.\n", mult);
    printf("Divis.: %d.\n", divi);

}