using System;
using System.Collections.Generic;


namespace Algorithms
{
    class Algorithms
    {
        static void Main(string[] args)
        {
            int[] arr = { 5, 3, 7, 9, 2, 1 };
            int smallest = FindSmallest(arr);
            System.Console.WriteLine($"Index of the smallest number in the array is: {smallest}");

            System.Console.WriteLine("Before SelectionSort()");
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

            System.Console.WriteLine("Array sum: ");

            LinkedList<int> llist = new LinkedList<int>(arr);
            
            Console.WriteLine("llist length: ");
            System.Console.WriteLine(Count(llist));
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

        public static int Count(LinkedList<int> arr)
        {
            int count = 0;
            if (arr == null)
            {
                System.Console.WriteLine("List is empty");
                return 0;
            }
            else
            {
                while (arr.First != null)
                {
                    arr.RemoveLast();
                    count++;
                    Count(arr);
                }
                
                
                //Count(arr);
            }
            return count;
        }


    }


}