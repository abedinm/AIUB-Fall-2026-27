using System;

enum Day { Sat, Sun, Mon = 10, Tue, Wed }

class Program
{
    static void Main()
    {
        Day d = Day.Sun;
        Console.WriteLine(d);
        Console.WriteLine((int)d);
        Console.WriteLine((int)Day.Tue);
        Console.WriteLine(Day.Wed);
    }
}