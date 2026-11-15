using System;

class MyDate
{
    private int day;
    private int month;
    private int year;

    public MyDate(int day, int month, int year)
    {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public void ShowDate()
    {
        Console.WriteLine("Joined: " + day + "/" + month + "/" + year);
    }
}

class Employee
{
    private string id;
    private string name;
    private double salary;
    private MyDate joiningDate;

    public string Id
    {
        get { return id; }
        set { id = value; }
    }

    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public double Salary
    {
        get { return salary; }
        set { salary = value; }
    }

    public Employee(string id, string name,
        double salary, MyDate joiningDate)
    {
        this.id = id;
        this.name = name;
        this.salary = salary;
        this.joiningDate = joiningDate;
    }

    public virtual void ShowInfo()
    {
        Console.WriteLine("ID: " + id);
        Console.WriteLine("Name: " + name);
        Console.WriteLine("Salary: " + salary);
        joiningDate.ShowDate();
    }

    public virtual void GrossIncome()
    {
        Console.WriteLine("Gross income: " + salary);
    }
}

class FullTime : Employee
{
    private double bonus;

    public FullTime(string id, string name,
        double salary, MyDate joiningDate, double bonus)
        : base(id, name, salary, joiningDate)
    {
        this.bonus = bonus;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Bonus: " + bonus);
    }

    public override void GrossIncome()
    {
        Console.WriteLine("Gross income: " + (Salary * 12 + bonus * 2));
    }
}

class PartTime : Employee
{
    private double commission;

    public PartTime(string id, string name,
        double salary, MyDate joiningDate, double commission)
        : base(id, name, salary, joiningDate)
    {
        this.commission = commission;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Commission: " + commission);
    }

    public override void GrossIncome()
    {
        Console.WriteLine("Gross income: " + (Salary + commission));
    }
}

class Program
{
    static void Main(string[] args)
    {
        Employee[] emp = new Employee[2];
        emp[0] = new FullTime("E-001", "Sarf", 30000,
            new MyDate(12, 09, 2013), 15000);
        emp[1] = new PartTime("E-002", "Kawsur", 12000,
            new MyDate(23, 07, 2019), 1300);

        foreach (Employee e in emp)
        {
            e.ShowInfo();
            e.GrossIncome();
            Console.WriteLine();
        }
    }
}
