#include <stdio.h>

int main(void) {

    int numb;
    int termo1 = 0;
    int termo2 = 1;
    int novoTermo;

    printf("Insira um numero: ");
    scanf("%d", &numb);

    for (int i = 0; i < numb; i++) {
    printf("%d ", termo1);
    novoTermo = termo1 + termo2;
    termo2 = termo1;
    termo1 = novoTermo;
    }

    return 0;
}