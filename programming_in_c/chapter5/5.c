/*
*You developed Program 4.9 to reverse the digits of an integer typed in
*from the terminal. However, this program does not function well if you
*type in a negative number. Find out what happens in such a case and then
*modify the program so that negative numbers are correctly handled. For
*example, if the number −8645 is typed in, the output of the program should
*be 5468−.
*/

#include <stdio.h>

int main()
{
    int number, right_digit, sign, mod_number;
    printf("Enter your numer.\n");
    scanf("%i", &number);

    sign = (number < 0) ? -1 : (number == 0) ? 0 : 1;
    mod_number = (sign == -1) ? (-1 * number) : number;
    //printf("mod_number = %i", mod_number);

    do
    {
        right_digit = mod_number % 10;
        printf("%i", right_digit);
        mod_number  = mod_number / 10;
    } while (mod_number != 0);

    (sign == -1) ? printf("-\n") : printf("\n");

    return 0;
    
}