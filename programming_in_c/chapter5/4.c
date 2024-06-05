/*
 * Write a program that acts as a simple “printing” calculator.
 * The program should allow the user to type in expressions of the form
 * number operator
 * The following operators should be recognized by the program:
 * + - * / S E
 * The S operator tells the program to set the “accumulator” to the typed-in
 * number. The E operator tells the program that execution is to end. The
 * arithmetic operations are performed on the contents of the accumulator
 * with the number that was keyed in acting as the second operand.
 *
 * */

#include <stdio.h>

int main()
{
	printf("Begin Calculations\n");
	float number, accumulator;
	char operator;

	scanf("%f %c", &number, &operator);	
	while (operator != 'E')
	{
		switch (operator)
		{
		case 'S':
			printf("= %f\n", accumulator = number);
			break;
		case '+':
			printf("= %f\n", accumulator += number);
			break;
		case '-':
			printf("= %f\n", accumulator -= number);
			break;
		case '*':
			printf("= %f\n", accumulator *= number);
			break;
		case '/':
			if (number == 0)
			{
				printf("Division by zero!\n");
				break;
			}
			else
			{
				printf("= %f\n", accumulator /= number);
				break;
			}
		default:
			printf("Unknown operator!");
			break;
		}

		scanf("%f %c", &number, &operator);	
	}
	printf("= %f\n", accumulator);
	printf("End of Calculations\n");
	
}