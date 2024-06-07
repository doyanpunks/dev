#include <stdio.h>

static int x =5;

int f(void)
{
    // static int x = 5;
    printf("%d\n", x);
    x++;
}

int main(void)
{
    f();
    f();
    f();

    return 0;
}
