using System;

class Student
{
    public int id;
    public string name;
    public static string uni;
    public static int count = 0;

    static Student()
    {
        uni = "AIUB";
        Console.WriteLine("static constructor");
    }

    public Student()
    {
        id = -1;
        name = "unknown";
        count++;
        Console.WriteLine("default constructor");
    }

    public Student(int id, string name)
    {
        this.id = id;
        this.name = name;
        count++;
        Console.WriteLine("parameterized constructor");
    }

    public Student(Student other)
    {
        id = other.id;
        name = other.name;
        count++;
        Console.WriteLine("copy constructor");
    }

    public void Show()
    {
        Console.WriteLine(id + " " + name + " " + uni);
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("Main starts");
        Student a = new Student();
        Student b = new Student(7, "Nila");
        Student c = new Student(b);
        c.name = "Rafi";
        a.Show();
        b.Show();
        c.Show();
        Console.WriteLine("count = " + Student.count);
    }
}