using System;

class Parent
{
}
class Child : Parent
{
}

class Program
{
    static void Main()
    {
        Child c = new Parent();
    }
}