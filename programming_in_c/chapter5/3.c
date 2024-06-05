/*
 * Write a program that accepts two integer values typed in by the user.
 * Display the result of dividing the first integer by the second, to three-
 * decimal-place accuracy. Remember to have the program check for
 * division by zero.
 */

#include <stdio.h>

int main()
{

	double a, b;
	printf("Enter two integers:\n");
	scanf("%lf",&a);
	scanf("%lf",&b);
	(b == 0) ? printf("Dibision by zero!\n") : printf("a / b = %.2f\n", a/b);
}
