using System;

class Calc
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }

    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }
}

class Program
{
    static void Main()
    {
        Calc k = new Calc();
        Console.WriteLine(k.Add(2, 3));
        Console.WriteLine(k.Add(2.5, 1.5));
        Console.WriteLine(k.Add(1, 2, 3));
    }
}