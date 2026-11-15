using System;

class Vehicle
{
    protected static int made = 0;
    protected string tag;

    public Vehicle()
    {
        made++;
        tag = "V" + made;
        Console.WriteLine("Vehicle " + tag);
    }

    public virtual void Info()
    {
        Console.WriteLine(tag + " is a vehicle");
    }

    public static void Count()
    {
        Console.WriteLine("Made: " + made);
    }
}
class Car : Vehicle
{
    private int seats;

    public Car(int seats)
    {
        this.seats = seats;
        Console.WriteLine("Car with " + seats + " seats");
    }

    public override void Info()
    {
        base.Info();
        Console.WriteLine(tag + " has " + seats + " seats");
    }
}
class Bus : Car
{
    public Bus() : base(40)
    {
        tag = tag + "-B";
        Console.WriteLine("Bus " + tag);
    }

    public new void Info()
    {
        Console.WriteLine(tag + " is a bus");
    }
}

class Program
{
    static void Main()
    {
        Vehicle v = new Car(4);
        Car c = new Bus();
        Bus b = (Bus)c;
        v.Info();
        c.Info();
        b.Info();
        Vehicle.Count();
    }
}