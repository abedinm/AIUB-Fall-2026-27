using System;

enum xyz { a, b, c, d }

class Program
{
    static void Main()
    {
        Console.WriteLine("{0}", (int)xyz.c);
    }
}