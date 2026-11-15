using System;


class Program
{
    static void Main()
    {
        int age = 20;
        double cgpa = 3.75;
        string name = "Nila";
        char grade = 'A';
        bool passed = true;

        Console.WriteLine(name + " is " + age);
        Console.WriteLine("CGPA: " + cgpa);
        Console.WriteLine("Passed: " + passed);
        Console.WriteLine("Sum: " + 2 + 3);
        Console.WriteLine(2 + 3 + " is the sum");
        Console.WriteLine(7 / 2);
        Console.WriteLine(7.0 / 2);
        Console.WriteLine(7 % 2);
        Console.WriteLine("{0} got {1}", name, grade);
    }
}