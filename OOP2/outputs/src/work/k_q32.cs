using System;


class Program
{
    static void Main()
    {
        int[][] t = new int[3][];
        t[0] = new int[] { 5, 10, 15, 20, 25 };
        t[1] = new int[3];
        t[2] = new int[] { 3, 6, 9 };

        for (int i = 0; i < t[1].Length; i++)
        {
            t[1][i] = t[0][i * 2] - t[2][i];
        }

        for (int r = t.Length - 1; r >= 0; r--)
        {
            for (int c = 0; c < t[r].Length; c += 2)
            {
                Console.Write("{0} ", t[r][c]);
            }
            Console.WriteLine();
        }

        int sum = 0;
        foreach (int[] row in t)
        {
            sum += row[row.Length - 1];
        }
        Console.WriteLine("Sum of last items = " + sum);
        Console.WriteLine(t[0].Length + t[1].Length * 2);
        Console.WriteLine("t[2][1] / 4 = " + t[2][1] / 4);
    }
}