#include <iostream>
#include <vector>

int main(void)
{
   std::vector<int> test_temp {73,74,75,71,69,72,76,73};
   for(int i = 0; i < test_temp.size() - 1; i++)
   {
      std::cout << i << std::endl;
   }
   return 0;
}

// 1-32. Write a function to perform integer division without using either the / or * operators. Find a fast way to do it.
int division(int a, int b)
{
   int count  = 0;
   int bb = b;
   if(a == b)
   {
      return 1;
   }
   else if(a == 1)
   {
      return b;
   }
   else
   {
      while(bb != 0)
      {
         bb = bb - a;
         count++;
      }
   }
   return count;
}

/*
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
*/

std::vector<int> daily_temp(const std::vector<int>& temp)
{
   int temp_size = temp.size();
   std::vector<int> answer;
   if(temp.empty() || temp.size() == 1)
   {
      return answer;
   }
   else
   {
      int i, j;
      int next = -1;
      for(i = 0; i < temp_size; i++ )
      {
         for(j = i + 1; j < temp_size; j++)
         {
            if(temp[i] < temp[j])
            {
               next = temp[j] - temp[i];
               answer.push_back(next);
            }
         }
      }
   }
}
