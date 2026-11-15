using System;

class Person
{
    protected string name = "Nila";
}

class Student : Person
{
    public void Show()
    {
        Console.WriteLine(name);
    }
}

class Program
{
    static void Main()
    {
        Student s = new Student();
        s.Show();
    }
}
