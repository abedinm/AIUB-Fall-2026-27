using System;


class Program
{
    static void Main()
    {
        int[] n = { 4, 7, 1, 9 };
        int big = n[0];
        foreach (int x in n)
        {
            if (x > big)
            {
                big = x;
            }
        }
        Console.WriteLine("big = " + big);
        n[2] = n[1] + n[3];
        Console.WriteLine(n[2]);
        Console.WriteLine(n.Length - 1);
    }
}