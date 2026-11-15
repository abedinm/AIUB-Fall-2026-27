using System;

class Employee
{
    private string name;
    private int id;

    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public int Id
    {
        get { return id; }
        set { id = value; }
    }

    public Employee(string name, int id)
    {
        this.name = name;
        this.id = id;
    }

    public virtual double CalculateSalary()
    {
        return 0;
    }
}

class FullTimeEmployee : Employee
{
    private double monthlySalary;

    public FullTimeEmployee(string name, int id, double monthlySalary) : base(name, id)
    {
        this.monthlySalary = monthlySalary;
    }

    public override double CalculateSalary()
    {
        return monthlySalary;
    }
}

class PartTimeEmployee : Employee
{
    private double hourlyRate;
    private int hoursWorked;

    public PartTimeEmployee(string name, int id, double hourlyRate, int hoursWorked) : base(name, id)
    {
        this.hourlyRate = hourlyRate;
        this.hoursWorked = hoursWorked;
    }

    public override double CalculateSalary()
    {
        return hourlyRate * hoursWorked;
    }
}

class SeniorEmployee : FullTimeEmployee
{
    private double bonus;

    public SeniorEmployee(string name, int id, double monthlySalary, double bonus)
        : base(name, id, monthlySalary)
    {
        this.bonus = bonus;
    }

    public override double CalculateSalary()
    {
        return base.CalculateSalary() + bonus;
    }

    public double Bonus
    {
        get { return bonus; }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Employee[] employees = new Employee[3];
        employees[0] = new FullTimeEmployee("Rafi", 1, 50000);
        employees[1] = new PartTimeEmployee("Nila", 2, 300, 40);
        employees[2] = new SeniorEmployee("Karim", 3, 60000, 10000);

        int[][] hours =
        {
            new int[] { 8, 8, 8, 8, 8 },
            new int[] { 5, 6, 4, 5, 6, 4, 5, 5 },
            new int[] { 9, 9, 10, 9, 9, 8 }
        };

        for (int i = 0; i < employees.Length; i++)
        {
            Console.WriteLine("ID: " + employees[i].Id + ", Name: " + employees[i].Name
                + ", Salary: " + employees[i].CalculateSalary());
            Console.Write("Hours: ");
            foreach (int h in hours[i])
            {
                Console.Write(h + " ");
            }
            Console.WriteLine();
        }

        if (employees[2] is SeniorEmployee)
        {
            SeniorEmployee senior = (SeniorEmployee)employees[2];
            Console.WriteLine(senior.Name + " gets a bonus of " + senior.Bonus);
        }
    }
}