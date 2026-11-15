using System;

class Student
{
    private string studentId;
    private string name;
    private double cgpa;

    public string StudentId
    {
        get { return studentId; }
        set { studentId = value; }
    }

    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public double Cgpa
    {
        get { return cgpa; }
        set { cgpa = value; }
    }

    public Student(string studentId,
        string name, double cgpa)
    {
        this.studentId = studentId;
        this.name = name;
        this.cgpa = cgpa;
    }

    public virtual bool IsEligible()
    {
        return false;
    }

    public virtual void ShowInfo()
    {
        Console.WriteLine("ID: " + studentId);
        Console.WriteLine("Name: " + name);
        Console.WriteLine("CGPA: " + cgpa);
    }
}

class Undergraduate : Student
{
    private int completedCredits;

    public Undergraduate(string studentId,
        string name, double cgpa,
        int completedCredits)
        : base(studentId, name, cgpa)
    {
        this.completedCredits = completedCredits;
    }

    public override bool IsEligible()
    {
        return Cgpa >= 3.75 && completedCredits >= 30;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Credits: " + completedCredits);
        if (IsEligible())
        {
            Console.WriteLine("Scholarship: Yes");
        }
        else
        {
            Console.WriteLine("Scholarship: No");
        }
    }
}

class Graduate : Student
{
    private int publications;

    public Graduate(string studentId,
        string name, double cgpa,
        int publications)
        : base(studentId, name, cgpa)
    {
        this.publications = publications;
    }

    public override bool IsEligible()
    {
        return Cgpa >= 3.5 && publications >= 2;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Publications: " + publications);
        if (IsEligible())
        {
            Console.WriteLine("Scholarship: Yes");
        }
        else
        {
            Console.WriteLine("Scholarship: No");
        }
    }
}

class Athlete : Student
{
    private int medals;

    public Athlete(string studentId,
        string name, double cgpa, int medals)
        : base(studentId, name, cgpa)
    {
        this.medals = medals;
    }

    public override bool IsEligible()
    {
        return Cgpa >= 2.5 && medals >= 3;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();
        Console.WriteLine("Medals: " + medals);
        if (IsEligible())
        {
            Console.WriteLine("Scholarship: Yes");
        }
        else
        {
            Console.WriteLine("Scholarship: No");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Student[] list = new Student[4];
        list[0] = new Undergraduate("22-1001-1", "Nila", 3.86, 45);
        list[1] = new Graduate("21-2002-2", "Rafi", 3.60, 1);
        list[2] = new Athlete("23-3003-3", "Karim", 2.75, 4);
        list[3] = new Undergraduate("22-4004-1", "Mim", 3.80, 24);

        foreach (Student s in list)
        {
            s.ShowInfo();
            Console.WriteLine();
        }
    }
}