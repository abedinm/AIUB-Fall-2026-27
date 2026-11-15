using System;

class Staff
{
    // STEP 1  fields: the data it keeps
    private string name;
    private int staffID;
    private double basePay;

    // STEP 2  properties: public doors
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public int StaffID
    {
        get { return staffID; }
        set { staffID = value; }
    }

    public double BasePay
    {
        get { return basePay; }
        set { basePay = value; }
    }

    // STEP 3  default constructor
    public Staff()
    {
        name = "";
        staffID = 0;
        basePay = 0.0;
    }

    // STEP 4  parameterized constructor
    public Staff(string name, int staffID, double basePay)
    {
        this.name = name;
        this.staffID = staffID;
        this.basePay = basePay;
    }

    // STEP 5  method: prints the details
    public void display_info()
    {
        Console.WriteLine("Name: " + name);
        Console.WriteLine("Staff ID: " + staffID);
        Console.WriteLine("Base pay: " + basePay);
    }
}

class Program
{
    // STEP 6  Main: make objects, use them
    static void Main(string[] args)
    {
        Staff s1 = new Staff();
        Staff s2 = new Staff("Rahim", 101, 45000.50);

        s1.display_info();
        Console.WriteLine();
        s2.display_info();

        s1.Name = "Karim";
        Console.WriteLine(s1.Name);
    }
}