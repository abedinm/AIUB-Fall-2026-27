using System;

abstract class Shape
{
    public abstract double Area();

    public void Print()
    {
        Console.WriteLine("Area = " + Area());
    }
}
class Square : Shape
{
    private double side;

    public Square(double side)
    {
        this.side = side;
    }

    public override double Area()
    {
        return side * side;
    }
}

class Program
{
    static void Main()
    {
        Shape s = new Square(3);
        s.Print();
    }
}