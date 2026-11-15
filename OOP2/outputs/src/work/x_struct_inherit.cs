using System;

class Base
{
}
struct S : Base
{
}

class Program
{
    static void Main()
    {
        S s = new S();
    }
}