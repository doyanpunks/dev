/*
 * chapter 4, ex 11
 * Write a program that calculates the sum of the digits of an integer. For
 * example, the sum of the digits of the number 2155 is 2 + 1 + 5 + 5 or 13.
 * The program should accept any arbitrary integer typed in by the user.
*/

#include <stdio.h>

int main(void)
{
	int number, digit;
	int sum = 0;
	printf("Enter the number:");
	scanf("%i", &number);
	while(number != 0)
	{
		digit = number % 10;
		sum += digit;
		number = number / 10;
	}

	printf("Sum of the digits in the number is: %d\n", sum);
	return 0;
}


