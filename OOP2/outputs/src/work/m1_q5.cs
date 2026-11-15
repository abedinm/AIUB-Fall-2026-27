using System;


class Program
{
    static void Main()
    {
        int[][] g = new int[3][];
        g[0] = new int[] { 2, 4, 6, 8 };
        g[1] = new int[] { 1, 3 };
        g[2] = new int[3];

        for (int i = 0; i < g[2].Length; i++)
        {
            g[2][i] = g[0][i] + g[0][i + 1];
        }

        for (int r = 0; r < g.Length; r++)
        {
            for (int c = 0; c < g[r].Length; c += 2)
            {
                Console.Write(g[r][c] + " ");
            }
            Console.WriteLine();
        }
    }
}