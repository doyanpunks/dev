#include <stdio.h>

int main(void)
{
    int Fibonacci[15];
    int i;
    Fibonacci[0] = 0;
    Fibonacci[1] = 1;

    for (i = 2; i < 15; ++i)
    {
        Fibonacci[i] = Fibonacci[i-2] + Fibonacci[i-1];
    }
    for (int i = 0; i < 15 ; ++i)
    {
        printf("%i\n", Fibonacci[i]);
    }

    return 0;
}