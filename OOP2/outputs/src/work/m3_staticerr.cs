using System;

class Shop
{
    private int items = 3;

    public static void Show()
    {
        Console.WriteLine(items);
    }
}

class Program
{
    static void Main()
    {
        Shop.Show();
    }
}