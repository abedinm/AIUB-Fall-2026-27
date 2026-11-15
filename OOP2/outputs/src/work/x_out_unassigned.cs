using System;


class Program
{
    static void F(out int a)
    {
    }
    static void Main()
    {
        int x;
        F(out x);
    }
}