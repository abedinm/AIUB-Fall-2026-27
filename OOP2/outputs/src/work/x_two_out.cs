using System;


class Program
{
    static void Two(out int a, out int b)
    {
        a = 3;
        b = 4;
    }
    static void Main()
    {
        int p, q;
        Two(out p, out q);
        Console.WriteLine(p * q);
    }
}