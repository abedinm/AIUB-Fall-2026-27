using System;


class Program
{
    static void Main()
    {
        int n = 10;
        object o = n;
        int back = (int)o;
        Console.WriteLine(o);
        Console.WriteLine(back + 1);

        var word = "Hi";
        var num = 5;
        Console.WriteLine(word + num);

        dynamic d = 10;
        Console.WriteLine(d);
        d = "now text";
        Console.WriteLine(d);

        int? age = null;
        Console.WriteLine(age);
        age = 20;
        Console.WriteLine(age);

        Console.WriteLine(n.GetType());
        Console.WriteLine(word.GetType());
    }
}