using System;


class Program
{
    static void Main()
    {
        int[][] jaggedArray = new int[2][];
        jaggedArray[0] = new int[] { 1, 2 };
        jaggedArray[1] = new int[] { 3, 4, 5 };
        Console.WriteLine(jaggedArray[1][3]);
    }
}