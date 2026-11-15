using System;

class Book
{
    ______ string title;
    private double price;

    public string Title
    {
        get { ______ title; }
        set { title = ______; }
    }

    public double Price
    {
        get { return price; }
        set { price = value; }
    }

    public ______()
    {
        title = "None";
        price = 0;
    }

    public Book(string title, double price)
    {
        ______.title = title;
        this.price = price;
    }

    public ______ ShowInfo()
    {
        Console.WriteLine(title + " costs " + price);
    }
}

class Program
{
    static void Main()
    {
        Book b1 = ______ Book();
        Book b2 = new Book("C# Basics", 450.5);
        b1.ShowInfo();
        b2.ShowInfo();
        b1.______ = 200;
        Console.WriteLine(b1.Price);
    }
}