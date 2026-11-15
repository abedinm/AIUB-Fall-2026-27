using System;

class Book
{
    private string title;
    private double price;

    public string Title
    {
        get { return title; }
        set { title = value; }
    }

    public double Price
    {
        get { return price; }
        set { price = value; }
    }

    public Book()
    {
        title = "None";
        price = 0;
    }

    public Book(string title, double price)
    {
        this.title = title;
        this.price = price;
    }

    public void ShowInfo()
    {
        Console.WriteLine(title + " costs " + price);
    }
}

class Program
{
    static void Main()
    {
        Book b1 = new Book();
        Book b2 = new Book("C# Basics", 450.5);
        b1.ShowInfo();
        b2.ShowInfo();
        b1.Price = 200;
        Console.WriteLine(b1.Price);
    }
}