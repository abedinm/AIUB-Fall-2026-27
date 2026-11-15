class Student
{
    private double cgpa;
    public double Cgpa
    {
        get { return cgpa; }
    }
    public Student(double cgpa)
    {
        this.cgpa = cgpa;
    }
}
class Graduate : Student
{
    public Graduate(double cgpa) : base(cgpa) { }
    public bool Good()
    {
        return cgpa >= 3.5;
    }
}
