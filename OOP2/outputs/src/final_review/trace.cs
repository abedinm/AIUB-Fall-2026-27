using System;

class Person
{
    protected static int count = 0;
    protected string name;

    public Person(string name)
    {
        this.name = name;
        count++;
        Console.WriteLine("Person " + name);
    }

    public virtual void Show()
    {
        Console.Write(name + " ");
    }
}

class Student : Person
{
    private double cgpa;

    public Student(string name, double cgpa) : base(name)
    {
        this.cgpa = cgpa;
        Console.WriteLine("Student " + cgpa);
    }

    public override void Show()
    {
        base.Show();
        Console.WriteLine(cgpa);
    }

    public static int Count()
    {
        return count;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Person p = new Student("Nila", 3.80);
        p.Show();
        Student s = new Student("Rafi", 3.5);
        s.Show();
        Console.WriteLine("count = " + Student.Count());
    }
}
