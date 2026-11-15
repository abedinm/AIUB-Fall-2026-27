using System;


class Program
{
    static void Main()
    {
        Student[] list = new Student[4];
        list[0] = new Undergraduate("22-1001-1", "Nila", 3.86, 45);
        list[1] = new Graduate("21-2002-2", "Rafi", 3.60, 1);
        list[2] = new Athlete("23-3003-3", "Karim", 2.75, 4);
        list[3] = new Undergraduate("22-4004-1", "Mim", 3.80, 24);

        foreach (Student s in list)
        {
            s.ShowInfo();
            Console.WriteLine();
        }
    }
}