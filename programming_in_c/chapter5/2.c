/* Write a program that asks the user to type in two integer values at the
* terminal. Test these two numbers to determine if the first is evenly
* divisible by the second, and then display an appropriate message at the
* terminal.
* */

#include <stdio.h>

int main()
{
	// delimoe
	int divident;

	// delitel
	int divider;
	printf("Enter two integers:\n");
	scanf("%i", &divident);
	scanf("%i", &divider);

	//chastnoe
	double quotient = divident / divider;

	printf("%d / %d = %.2f\n", divident, divider, quotient);

	(divident % divider == 0) ? printf("%d is evenly divisible by the %d\n", divident, divider) : printf("%d is not evenly divisible by the %d\n", divident, divider);

	return 0;
}
