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
