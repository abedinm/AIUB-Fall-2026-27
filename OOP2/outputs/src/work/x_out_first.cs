using System;


class Program
{
    static void F(out int a, int b)
    {
        a = b * 2;
    }
    static void Main()
    {
        int x;
        F(out x, 4);
        Console.WriteLine(x);
    }
}