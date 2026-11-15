using System;

class Teacher
{
    private int salary = 50000;
    protected string subject = "C#";
}

class Program
{
    static void Main()
    {
        Teacher t = new Teacher();
        Console.WriteLine(t.salary);
        Console.WriteLine(t.subject);
    }
}