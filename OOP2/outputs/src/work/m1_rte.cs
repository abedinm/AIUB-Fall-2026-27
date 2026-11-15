using System;


class Program
{
    static void Main()
    {
        int[][] j = new int[2][];
        j[0] = new int[] { 1, 2 };
        j[1] = new int[] { 3, 4, 5 };
        Console.WriteLine(j[1][2]);
        Console.WriteLine(j[0][2]);
    }
}