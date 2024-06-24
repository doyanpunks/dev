#include <stdio.h>

int main(void)
{
    int numbers[10] = {1,0,0,0,0,0,0,0,0,0};
    int i,j;

    for (i = 0; i < 10; ++i)
    {
        for (j = 0; j < 10; ++j)
        {
            numbers[j] += numbers[i];
        }
    }
    for (j = 0; j < 10; ++j)
    {
        printf("%i", numbers[j]);
    }
    printf("\n");

}