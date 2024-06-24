/*
Program 6.2 permits only 20 responses to be entered. Modify that
program so that any number of responses can be entered. So that the user
does not have to count the number of responses in the list, set up the
program so that the value 999 can be keyed in by the user to indicate that
the last response has been entered. (Hint: You can use the break
statement here if you want to exit your loop.)
*/

#include <stdio.h>

int main()
{
    int  i;
    unsigned long long int response, ratingCounters[11];

    for (int i = 0; i < 10; ++i)
    {
        ratingCounters[i] = 0;
    }

    printf("Enter your response\n");

    for (int i = 0; i <= 20; ++i)
    {
        scanf("%llu", &response);
        if (response == 999)
        {
            printf("Bad response: %llu\n", response);
            break;
        }
        else
        {
            ++ratingCounters[response];
        }

        printf("\n\nRating  Number of Responses\n");
        printf("------ -------------------\n");

        for (int i = 1; i <= 10; ++i)
        {
            printf("%14lli\n", i, ratingCounters[i]);
        }
        
    }
    
    return 0;
}