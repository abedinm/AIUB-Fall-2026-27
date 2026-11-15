using System;


class Program
{
    static void F(ref int a)
    {
    }
    static void Main()
    {
        F(ref 5);
    }
}