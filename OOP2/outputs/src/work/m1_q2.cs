using System;


class Program
{
    static void Main()
    {
        double m = 9.99;
        int n = (int)m;
        char c = 'C';
        Console.WriteLine(n);
        Console.WriteLine((int)c);
        Console.WriteLine(n + m);
        bool ok = n > 9;
        Console.WriteLine(ok);
        n *= 2;
        n--;
        Console.WriteLine("n = " + n);
        Console.WriteLine("Done\nNow");
    }
}