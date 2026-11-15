using System;
class Parent
{
    private string id;
    private double cgpa;
    public double Cgpa { get { return cgpa; } }
    public Parent(string id, double cgpa) { this.id = id; this.cgpa = cgpa; }
    public virtual bool IsEligible() { return false; }
    public virtual void ShowInfo() { Console.WriteLine("ID: " + id); }
}
class Child : Parent
{
    private int extra;          // only the child's own field

    public Child(string id, double cgpa, int extra)
        : base(id, cgpa)        // parent's values go UP
    {
        this.extra = extra;
    }

    public override bool IsEligible()
    {
        // parent's field is private: use its property
        return Cgpa >= 3.5 && extra >= 2;
    }

    public override void ShowInfo()
    {
        base.ShowInfo();        // parent's lines first
        Console.WriteLine("Extra: " + extra);
        if (IsEligible())
        {
            Console.WriteLine("Eligible: Yes");
        }
        else
        {
            Console.WriteLine("Eligible: No");
        }
    }                           // ShowInfo ends after else
}
class Program { static void Main() { Parent p = new Child("S-1", 3.6, 2); p.ShowInfo(); } }
