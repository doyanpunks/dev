#include <iostream>
#include <cmath>
#include <direct.h>
int main()
{
    const double COST_PER_SQ_FT = 10.50;
    double budget, area, lengthSide;

    std::cout << "Enter the amount budgeted for your dogouse $: ";
    std::cin >> budget;

    area = budget / COST_PER_SQ_FT;
    lengthSide = sqrt(area);

    std::cout.setf(std::ios::fixed);
    std::cout.setf(std::ios::showpoint);
    std::cout.precision(2);
    std::cout << "For a price of $" << budget << std::endl
        << "I can build you a luxurious square doghouse\n"
        << "that is " << lengthSide
        << " feet on each side.\n";

    return 0;
}