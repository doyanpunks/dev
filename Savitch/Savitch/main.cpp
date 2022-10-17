#include <iostream>
#include "main.h"

int main()
{
	std::cout << mystery(10, 9) << "OW\n";
	std::cout << zero_or_negative(-5.6) << std::endl;
	std::cout << "video clip bitrate is 55 kbit/s" << std::endl;
	std::cout << video_size(55, 180) << std::endl;
	return 0;
}

char mystery(int first, int second)
{
	if (first >= second)
	{
		return 'W';
	}
	else
	{
		return 'H';
	}
}
char zero_or_negative(double test_var)
{
	if (test_var > 0)
	{
		return 'P';
	}
	else
	{
		return 'N';
	}
}
double video_size(int bit_rate, int duration_min)
{
	double duration_sec = duration_min / 60;
	return (bit_rate* duration_sec) * one_megabyte;
}
int sum(int first, int second)
{
	return first + second;
}
double gravity_force()
{
	
	return (G * m1 * m2) / d*d;
}