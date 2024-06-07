/*
* Write a program that takes an integer keyed in from the terminal and
* extracts and displays each digit of the integer in English. So, if the user
* types in 932, the program should display
* nine three two
* Remember to display “zero” if the user types in just a 0. (Note: This
* exercise is a hard one!)
*/

#include <stdio.h>

int main()
{
   int number;
   printf("Enter the number: \n");
   scanf("%d", &number);

   if (number == 0)
   {
      printf("zero");
   }
   

    int number_to_convert;
    switch (number_to_convert)
    {
    case 1:
        printf("one ");
        break;
     case 2:
        printf("two ");
        break;   
     case 3:
        printf("three ");
        break;   
     case 4:
        printf("four ");
        break;   
     case 5:
        printf("five ");
        break;   
     case 6:
        printf("six ");
        break;   
     case 7:
        printf("seven ");
        break;   
     case 8:
        printf("eight ");
        break;   
     case 9:
        printf("nine ");
        break;   
    default:
        printf("Unknown number or negative number!");
        break;
    }
}