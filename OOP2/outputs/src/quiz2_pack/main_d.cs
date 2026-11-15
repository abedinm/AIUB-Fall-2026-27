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
