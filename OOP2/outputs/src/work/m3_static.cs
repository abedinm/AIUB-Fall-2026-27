using System;

class Counter
{
    public static int total = 0;
    public int mine = 0;
    public const double Rate = 0.5;
    public readonly int id;

    public Counter(int id)
    {
        this.id = id;
        total++;
        mine++;
    }
}

class Program
{
    static void Main()
    {
        Counter a = new Counter(1);
        Counter b = new Counter(2);
        Console.WriteLine(Counter.total);
        Console.WriteLine(a.mine + " " + b.mine);
        Console.WriteLine(Counter.Rate);
        Console.WriteLine(a.id + " " + b.id);
    }
}