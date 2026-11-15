using System;

class Device
{
    protected string brand;

    public Device(string brand)
    {
        this.brand = brand;
        Console.WriteLine("Device " + brand);
    }

    public virtual void Info()
    {
        Console.WriteLine("Brand: " + brand);
    }
}

class Phone : Device
{
    protected int sims;

    public Phone(string brand, int sims) : base(brand)
    {
        this.sims = sims;
        Console.WriteLine("Phone " + sims);
    }

    public override void Info()
    {
        base.Info();
        Console.WriteLine("SIMs: " + sims);
    }
}

class SmartPhone : Phone
{
    private double screen;

    public SmartPhone(string brand, int sims, double screen)
        : base(brand, sims)
    {
        this.screen = screen;
        Console.WriteLine("SmartPhone " + screen);
    }

    public override void Info()
    {
        Console.WriteLine("Screen: " + screen);
        base.Info();
    }
}

class Program
{
    static void Main(string[] args)
    {
        Device[] list = new Device[2];
        list[0] = new SmartPhone("Walton", 2, 6.50);
        list[1] = new Device("Sony");
        Console.WriteLine("---");
        foreach (Device d in list)
        {
            d.Info();
        }
    }
}
