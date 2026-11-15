using System;

class Car
{
}
class Bike
{
    public override string ToString()
    {
        return "I am a bike";
    }
}

class Program
{
    static void Main()
    {
        Car c = new Car();
        Bike b = new Bike();
        Console.WriteLine(c);
        Console.WriteLine(b);
        Console.WriteLine(c.GetType());
    }
}