using System;

struct Point
{
    public int x;
    public int y;

    public Point(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
}
class Spot
{
    public int x;
}

class Program
{
    static void Main()
    {
        Point p1 = new Point(1, 2);
        Point p2 = p1;
        p2.x = 50;
        Console.WriteLine(p1.x + " " + p2.x);

        Spot s1 = new Spot();
        Spot s2 = s1;
        s2.x = 50;
        Console.WriteLine(s1.x + " " + s2.x);

        Console.WriteLine(p1);
    }
}