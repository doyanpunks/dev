using System;
using System.Collections.Generic;
using System.Linq;


namespace Algorithms
{
    class Algorithms
    {
        static void Main(string[] args)
        {
            int[] arr = { 5, 3, 7, 9, 2, 1 };
            //var test = arr.Skip(5);
            //var test = arr.Take(5);
            int smallest = FindSmallest(arr);

            Console.WriteLine($"Index of the smallest number in the array is: {smallest}");
            Console.WriteLine("Before SelectionSort()");
            for (int i = 0; i < arr.Length; i++)
            {
                System.Console.WriteLine(arr[i]);
            }

            System.Console.WriteLine("After SelectionSort()");

            int[] newarr = SelectionSort(arr);
            for (int i = 0; i < newarr.Length; i++)
            {
                System.Console.WriteLine(newarr[i]);
            }

            Console.WriteLine($"Array sum: {Sum(arr)}");
            Console.WriteLine($"llist length: {Count(arr)}");
            Console.WriteLine($"Max from list: {Max(arr)}");

            //foreach (var item in test)
            //{
            //    Console.WriteLine(item);
            //}

        }
        // it works!
        public static int FindSmallest(int[] arr)
        {
            int smallest = arr[0];
            int smallest_index = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] < smallest)
                {
                    smallest = arr[i];
                    smallest_index = i;
                }
            }
            return smallest_index;
        }
        // it works(I guess)
        public static int[] SelectionSort(int[] arr)

        {
            int[] newArr = new int[arr.Length];
            for (int i = 0; i < newArr.Length; i++)
            {
                int smallest = arr[FindSmallest(arr)];
                newArr[i] = smallest;
                arr = arr.Where(val => val != arr[FindSmallest(arr)]).ToArray();
            }
            return newArr;
        }
        public static int Sum(IEnumerable<int> list)
        {
            if (!list.Any())
            {
                return 0;
            }
            else
            {
                // For debugging
                //var first = list.Take(1).First();
                //var second = Sum(list.Skip(1));

                return list.Take(1).First() + Sum(list.Skip(1));
            }
        }
        public static int Count(IEnumerable<int> list)
        {
            if (!list.Any())
            {
                return 0;
                Console.WriteLine("List is empty");
            }
            else
            {
                return 1 + Count(list.Skip(1));
            }
        }
        public static int Max(IEnumerable<int> list)
        {
            if (!list.Any())
            {
                return 0;
                Console.WriteLine("List is empty");
            }
            if (Count(list) == 1)
            {
                return list.First();
            }
            else
            {
                var sub_max = Max(list.Skip(1));
                return list.First() > sub_max ? list.First() : sub_max;
                
            }
        }
    }
}