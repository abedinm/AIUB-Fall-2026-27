using System;


class Program
{
    static void Main()
    {
        int[] a = { 10, 20, 30 };
        Console.WriteLine(a[0]);
        Console.WriteLine(a.Length);

        int[] b = new int[3];
        Console.WriteLine(b[1]);

        int[] c = a;
        c[0] = 99;
        Console.WriteLine(a[0]);

        for (int i = a.Length - 1; i >= 0; i--)
        {
            Console.Write(a[i] + " ");
        }
        Console.WriteLine();
    }
}