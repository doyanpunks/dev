/*
Write a program that calculates the average of an array of 10 floating-
point values.
*/

#include <stdio.h>

int main(void)
{
    int arr_length = 10;
    double arr[arr_length];
    double avg = 0;
    double sum = 0;

    printf("Enter 10 floating point values: ");

    for (int i = 0; i < arr_length; ++i)
    {
        scanf("%lf", &arr[i]);
    }

    for (int i = 0; i < arr_length; ++i)
    {
        sum = sum + arr[i];
        avg = sum / 10;
        //printf("%.5lf\n", arr[i]);
    }

    printf("average is: %lf\n", avg);
    printf("sum is: %lf\n", sum);

    return 0;
}