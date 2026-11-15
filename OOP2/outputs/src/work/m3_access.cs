using System;

class Teacher
{
    public string name = "Rafi";
    private int salary = 50000;
    protected string subject = "C#";
    internal string dept = "CSE";
    protected internal string room = "9310K";

    public int GetSalary()
    {
        return salary;
    }
}
class Senior : Teacher
{
    public void Show()
    {
        Console.WriteLine(subject + " " + room + " " + dept);
    }
}

class Program
{
    static void Main()
    {
        Teacher t = new Teacher();
        Console.WriteLine(t.name + " " + t.GetSalary());
        Console.WriteLine(t.dept + " " + t.room);
        Senior s = new Senior();
        s.Show();
    }
}