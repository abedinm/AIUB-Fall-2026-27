using System;

abstract class Shape
{
    protected string name;

    public Shape(string name)
    {
        this.name = name;
    }
}
class Circle : Shape
{
    public Circle() : base("circle")
    {
        Console.WriteLine(name);
    }
}

class Program
{
    static void Main()
    {
        Shape s = new Circle();
    }
}