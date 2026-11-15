using System;


class Program
{
    static void F(params int[] x)
    {
        Console.WriteLine(x.Length);
    }
    static void Main()
    {
        F();
        F(1, 2);
        F(new int[] { 1, 2, 3 });
    }
}