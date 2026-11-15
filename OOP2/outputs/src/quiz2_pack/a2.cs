using System;

class Account
{
    protected double balance;
    public static int count = 0;

    public Account(double balance)
    {
        this.balance = balance;
        count++;
    }

    public virtual void Monthly()
    {
        balance = balance + 100;
    }

    public void Show()
    {
        Console.WriteLine("Account " + balance);
    }
}

class Savings : Account
{
    public Savings(double balance) : base(balance)
    {
    }

    public override void Monthly()
    {
        base.Monthly();
        balance = balance * 2;
    }

    public new void Show()
    {
        Console.WriteLine("Savings " + balance);
    }
}

class Program
{
    static void Main(string[] args)
    {
        Account a = new Savings(50);
        Savings s = new Savings(10);
        Account b = new Account(5);
        a.Monthly();
        s.Monthly();
        b.Monthly();
        a.Show();
        s.Show();
        ((Savings)a).Show();
        b.Show();
        Console.WriteLine(a is Savings);
        Console.WriteLine(b is Savings);
        Console.WriteLine("count = " + Account.count);
    }
}
