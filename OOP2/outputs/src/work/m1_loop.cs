using System;


class Program
{
    static void Main()
    {
        for (int i = 1; i <= 3; i++)
        {
            Console.WriteLine("i = " + i);
        }

        int total = 0;
        for (int i = 0; i < 6; i += 2)
        {
            total += i;
        }
        Console.WriteLine("total = " + total);

        int[] marks = { 70, 85, 40 };
        foreach (int m in marks)
        {
            if (m >= 50)
            {
                Console.WriteLine(m + " pass");
            }
            else
            {
                Console.WriteLine(m + " fail");
            }
        }
    }
}