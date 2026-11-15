using System;


class Program
{
    static void NoRef(int x)
    {
        x = x + 5;
    }
    static void AddFive(ref int x)
    {
        x = x + 5;
    }
    static void GetTwo(out int a, out int b)
    {
        a = 1;
        b = 2;
    }
    static int Sum(params int[] nums)
    {
        int s = 0;
        foreach (int n in nums)
        {
            s += n;
        }
        return s;
    }
    static void Main()
    {
        int v = 10;
        NoRef(v);
        Console.WriteLine(v);
        AddFive(ref v);
        Console.WriteLine(v);

        int p, q;
        GetTwo(out p, out q);
        Console.WriteLine(p + q);

        Console.WriteLine(Sum());
        Console.WriteLine(Sum(4));
        Console.WriteLine(Sum(1, 2, 3));
    }
}