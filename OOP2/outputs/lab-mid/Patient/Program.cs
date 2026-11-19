using System;

namespace HealthcareSystem
{
    class Patient
    {
        private string name;
        private int age;
        private string patientId;

        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        public int Age
        {
            get { return age; }
            set { age = value; }
        }

        public string PatientId
        {
            get { return patientId; }
            set { patientId = value; }
        }

        public Patient(string name, int age, string patientId)
        {
            this.name = name;
            this.age = age;
            this.patientId = patientId;
        }

        public virtual void CalculateReport()
        {
            Console.WriteLine("Report: basic check-up");
        }

        public virtual void ShowInfo()
        {
            Console.WriteLine("ID: " + patientId + ", Name: " + name + ", Age: " + age);
        }
    }

    class GeneralPatient : Patient
    {
        private string problem;

        public GeneralPatient(string name, int age, string patientId, string problem)
            : base(name, age, patientId)
        {
            this.problem = problem;
        }

        public override void CalculateReport()
        {
            Console.WriteLine("Report: general patient, problem: " + problem);
        }
    }

    class DiabeticPatient : Patient
    {
        private double sugarLevel;

        public DiabeticPatient(string name, int age, string patientId, double sugarLevel)
            : base(name, age, patientId)
        {
            this.sugarLevel = sugarLevel;
        }

        public override void CalculateReport()
        {
            Console.WriteLine("Report: diabetic patient, sugar level: " + sugarLevel);
            if (sugarLevel >= 7.0)
            {
                Console.WriteLine("Status: High");
            }
            else
            {
                Console.WriteLine("Status: Normal");
            }
        }
    }

    class HeartPatient : Patient
    {
        private int heartRate;

        public HeartPatient(string name, int age, string patientId, int heartRate)
            : base(name, age, patientId)
        {
            this.heartRate = heartRate;
        }

        public override void CalculateReport()
        {
            Console.WriteLine("Report: heart patient, heart rate: " + heartRate + " bpm");
        }
    }

    class CriticalHeartPatient : HeartPatient
    {
        private int oxygenLevel;

        public int OxygenLevel
        {
            get { return oxygenLevel; }
            set { oxygenLevel = value; }
        }

        public CriticalHeartPatient(string name, int age, string patientId, int heartRate, int oxygenLevel)
            : base(name, age, patientId, heartRate)
        {
            this.oxygenLevel = oxygenLevel;
        }

        public override void CalculateReport()
        {
            base.CalculateReport();
            Console.WriteLine("Critical: oxygen level " + oxygenLevel + "%, needs ICU monitoring");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Patient[] patients = new Patient[4];
            patients[0] = new GeneralPatient("Rahim", 30, "P-01", "Fever");
            patients[1] = new DiabeticPatient("Karim", 55, "P-02", 8.2);
            patients[2] = new HeartPatient("Nila", 48, "P-03", 95);
            patients[3] = new CriticalHeartPatient("Rafi", 62, "P-04", 130, 88);

            double[][] readings = new double[4][];
            readings[0] = new double[] { 98.6, 99.1 };
            readings[1] = new double[] { 8.2, 7.9, 8.5 };
            readings[2] = new double[] { 95, 92, 97, 94 };
            readings[3] = new double[] { 130 };

            for (int i = 0; i < patients.Length; i++)
            {
                patients[i].ShowInfo();
                patients[i].CalculateReport();
                Console.Write("Readings: ");
                for (int j = 0; j < readings[i].Length; j++)
                {
                    Console.Write(readings[i][j] + " ");
                }
                Console.WriteLine();
                Console.WriteLine();
            }

            Console.WriteLine("--- Typecasting ---");
            Patient p = new CriticalHeartPatient("Mim", 70, "P-05", 140, 85);
            p.CalculateReport();

            if (p is CriticalHeartPatient)
            {
                CriticalHeartPatient c = (CriticalHeartPatient)p;
                Console.WriteLine("Downcast: oxygen level " + c.OxygenLevel + "%");
            }

            HeartPatient h = (HeartPatient)p;
            Console.WriteLine("HeartPatient reference name: " + h.Name);

            Console.ReadLine();
        }
    }
}
