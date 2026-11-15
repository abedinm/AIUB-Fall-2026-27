using System;

class Box
{
    public readonly int size = 5;

    public void Grow()
    {
        size = 10;
    }
}

class Program
{
    static void Main()
    {
        Box b = new Box();
    }
}