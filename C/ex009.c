#include <stdio.h>

int main(void) {

    int soma = 0;
    int numb;

    printf("Insira um numero inteiro: ");
    scanf("%d", &numb);

    for (int i = 0; i <= numb; i++)
    {soma += i;
    printf("i = %d, soma = %d\n", i, soma);}

    printf("A soma de 1 a %d e igual a %d\n", numb, soma);

    return 0;
}
