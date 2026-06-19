#include <stdio.h> 

int main(void) {

    int ano;

    printf("Insira o ano: ");
    scanf("%d", &ano);

    if ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0))
    {printf("O ano %d e um Bissexto \n", ano);}

    else 
    {printf("O ano inserido nao e um Bissexto");}

    return 0;
}