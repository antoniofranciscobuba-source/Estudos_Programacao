#include <stdio.h>

int main(void) {
    
    float temperatura;
    printf("Conversao de Celsius para Fahrenheit\n");

    printf("Insira temperatura Celsius: ");
    scanf("%f\n", &temperatura);

    printf("%2.f Celsius e igual a: %.2f Fahrenheit",
    temperatura, temperatura * 9/5 + 32);
    /*fahre = celsius 9/5 + 32;*/
}