using System;


class Program
{
    static void Main()
    {
        int a = 9;
        int b = 4;
        Console.WriteLine(a / b);
        Console.WriteLine(a % b);
        Console.WriteLine("a + b = " + a + b);
        Console.WriteLine("a + b = " + (a + b));
        Console.Write(a);
        Console.Write(b);
        Console.WriteLine();
        Console.WriteLine("{1} {0}", a, b);
    }
}