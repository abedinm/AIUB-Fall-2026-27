using System;

class Person
{
    protected string name;

    public Person(string name)
    {
        this.name = name;
        Console.WriteLine("Person constructor");
    }

    public virtual void Show()
    {
        Console.WriteLine("Name: " + name);
    }
}
class Student : Person
{
    private double cgpa;

    public Student(string name, double cgpa) : base(name)
    {
        this.cgpa = cgpa;
        Console.WriteLine("Student constructor");
    }

    public override void Show()
    {
        base.Show();
        Console.WriteLine("CGPA: " + cgpa);
    }
}

class Program
{
    static void Main()
    {
        Person p = new Student("Nila", 3.8);
        p.Show();
    }
}