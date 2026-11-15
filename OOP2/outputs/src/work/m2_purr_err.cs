using System;

class Animal
{
    public virtual string Sound()
    {
        return "...";
    }
}
class Cat : Animal
{
    public void Purr()
    {
        Console.WriteLine("Purr");
    }
}

class Program
{
    static void Main()
    {
        Animal a = new Cat();
        a.Purr();
    }
}