using System;

class Parent
{
    public void Hi()
    {
    }
}
class Child : Parent
{
    public override void Hi()
    {
    }
}

class Program
{
    static void Main()
    {
        Child c = new Child();
    }
}