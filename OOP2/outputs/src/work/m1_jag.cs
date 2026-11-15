using System;


class Program
{
    static void Main()
    {
        int[][] j = new int[3][];
        j[0] = new int[] { 1, 2, 3 };
        j[1] = new int[] { 4, 5 };
        j[2] = new int[4];

        Console.WriteLine(j.Length);
        Console.WriteLine(j[0].Length);
        Console.WriteLine(j[1][1]);
        Console.WriteLine(j[2][3]);

        for (int r = 0; r < j.Length; r++)
        {
            for (int c = 0; c < j[r].Length; c++)
            {
                Console.Write(j[r][c] + " ");
            }
            Console.WriteLine();
        }

        foreach (int[] row in j)
        {
            Console.Write(row.Length + " ");
        }
        Console.WriteLine();
    }
}