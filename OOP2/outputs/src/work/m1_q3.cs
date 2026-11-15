using System;


class Program
{
    static void Main()
    {
        int sum = 0;
        for (int i = 1; i <= 5; i++)
        {
            if (i % 2 == 0)
            {
                sum += i;
            }
            else
            {
                Console.Write(i + " ");
            }
        }
        Console.WriteLine();
        Console.WriteLine("sum = " + sum);
    }
}