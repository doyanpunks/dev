/*
You don’t need to use an array to generate Fibonacci numbers. You can
simply use three variables: two to store the previous two Fibonacci
numbers and one to store the current one. Rewrite Program 6.3 so that
arrays are not used. Because you’re no longer using an array, you need to
display each Fibonacci number as you generate it.
*/

#include <stdio.h>

int main()
{
    int low = 0;
    int high = 1;
    int current = low + high;
    printf("%i ", low);
    printf("%i ", high);
    for (int i = 3; i <= 15; ++i)
    {
        printf("%i ", current);
        low = high;
        high = current;
        current = low + high;
    }
    
    printf("\n");
    return 0;
}