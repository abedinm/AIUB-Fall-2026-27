using System;

class Animal
{
    public virtual string Sound()
    {
        return "...";
    }
}
class Dog : Animal
{
    public override string Sound()
    {
        return "Woof";
    }
}
class Cat : Animal
{
    public override string Sound()
    {
        return "Meow";
    }

    public void Purr()
    {
        Console.WriteLine("Purr");
    }
}

class Program
{
    static void Main()
    {
        Animal[] pets = new Animal[3];
        pets[0] = new Dog();
        pets[1] = new Cat();
        pets[2] = new Animal();

        foreach (Animal a in pets)
        {
            Console.WriteLine(a.Sound());
        }

        if (pets[1] is Cat)
        {
            Cat c = (Cat)pets[1];
            c.Purr();
        }
    }
}