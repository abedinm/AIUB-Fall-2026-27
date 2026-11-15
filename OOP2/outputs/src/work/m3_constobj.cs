using System;

class Counter
{
    public const double Rate = 0.5;
}

class Program
{
    static void Main()
    {
        Counter a = new Counter();
        Console.WriteLine(a.Rate);
    }
}