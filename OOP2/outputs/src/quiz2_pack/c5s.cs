class Person
{
    protected string name = "Nila";
}
class Student : Person
{
    public void Show()
    {
        Console.WriteLine(name);
    }
}
// Main
Student s = new Student();
s.Show();
