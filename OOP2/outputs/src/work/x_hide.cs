using System;

class Parent
{
    public void Hi()
    {
        Console.WriteLine("Parent");
    }
}
class Child : Parent
{
    public void Hi()
    {
        Console.WriteLine("Child");
    }
}

class Program
{
    static void Main()
    {
        Parent p = new Child();
        p.Hi();
    }
}