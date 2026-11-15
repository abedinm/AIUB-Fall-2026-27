using System;

class Car
{
    private string model;

    public Car(string model)
    {
        this.model = model;
    }
}

class Program
{
    static void Main()
    {
        Car c = new Car();
    }
}