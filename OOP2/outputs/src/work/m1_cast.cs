using System;


class Program
{
    static void Main()
    {
        double price = 10.75;
        int whole = (int)price;
        Console.WriteLine(whole);

        int count = 10;
        double d = count;
        Console.WriteLine(d);

        char letter = 'A';
        int code = letter;
        Console.WriteLine(code);
        Console.WriteLine((char)66);
        Console.WriteLine(letter + 1);

        int x = 5;
        x += 3;
        x++;
        Console.WriteLine(x);
    }
}