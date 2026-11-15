using System;

class Vehicle
{
    private string vehicleId;
    private double dailyRent;

    public string VehicleId
    {
        get { return vehicleId; }
        set { vehicleId = value; }
    }

    public double DailyRent
    {
        get { return dailyRent; }
        set { dailyRent = value; }
    }

    public Vehicle(string vehicleId, double dailyRent)
    {
        this.vehicleId = vehicleId;
        this.dailyRent = dailyRent;
    }

    public virtual double Rent(int days)
    {
        return dailyRent * days;
    }

    public virtual void ShowInfo()
    {
        Console.WriteLine("ID: " + vehicleId);
        Console.WriteLine("Daily rent: " + dailyRent);
    }
}

class Car : Vehicle
{
    private int seats;

    public Car(string vehicleId, double dailyRent, int seats)
        : base(vehicleId, dailyRent)
    {
        this.seats = seats;
    }

    public override double Rent(int days)
    {
        double cost = base.Rent(days);
        if (seats > 5)
        {
            cost = cost + 500;
        }
        return cost;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Seats: " + seats);
    }
}

class Truck : Vehicle
{
    private double loadTons;

    public Truck(string vehicleId, double dailyRent, double loadTons)
        : base(vehicleId, dailyRent)
    {
        this.loadTons = loadTons;
    }

    public override double Rent(int days)
    {
        return base.Rent(days) + loadTons * 1000;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Load: " + loadTons + " tons");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Vehicle[] v = new Vehicle[3];
        v[0] = new Car("C-1", 3000, 7);
        v[1] = new Car("C-2", 2500, 4);
        v[2] = new Truck("T-1", 5000, 2.5);

        foreach (Vehicle x in v)
        {
            x.ShowInfo();
            Console.WriteLine("Rent for 3 days: " + x.Rent(3));
            Console.WriteLine();
        }
    }
}
