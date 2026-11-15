using System;

class Course
{
    private string courseCode;
    private string courseTitle;
    private int credit;

    public string CourseCode
    {
        get { return courseCode; }
        set { courseCode = value; }
    }

    public string CourseTitle
    {
        get { return courseTitle; }
        set { courseTitle = value; }
    }

    public int Credit
    {
        get { return credit; }
        set { credit = value; }
    }

    public Course()
    {
        courseCode = "N/A";
        courseTitle = "N/A";
        credit = 0;
    }

    public Course(string courseCode, string courseTitle, int credit)
    {
        this.courseCode = courseCode;
        this.courseTitle = courseTitle;
        this.credit = credit;
    }

    public void ShowCourse()
    {
        Console.WriteLine(courseCode + ", " + courseTitle + ", " + credit + " credits");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Course c1 = new Course();
        Course c2 = new Course("CSC 3115", "OOP 2", 3);
        c1.ShowCourse();
        c2.ShowCourse();
    }
}