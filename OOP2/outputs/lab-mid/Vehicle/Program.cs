using System;

namespace VehicleManagement
{
    class Vehicle
    {
        private string regNumber;
        private string brand;
        private int year;

        public string RegNumber
        {
            get { return regNumber; }
            set { regNumber = value; }
        }

        public string Brand
        {
            get { return brand; }
            set { brand = value; }
        }

        public int Year
        {
            get { return year; }
            set { year = value; }
        }

        public Vehicle(string regNumber, string brand, int year)
        {
            this.regNumber = regNumber;
            this.brand = brand;
            this.year = year;
        }

        public virtual double CalculateRental(int days)
        {
            return 1000 * days;
        }

        public virtual void ShowInfo()
        {
            Console.WriteLine("Reg: " + regNumber + ", Brand: " + brand + ", Year: " + year);
        }
    }

    class Car : Vehicle
    {
        private int seats;

        public Car(string regNumber, string brand, int year, int seats)
            : base(regNumber, brand, year)
        {
            this.seats = seats;
        }

        public override double CalculateRental(int days)
        {
            return 2000 * days + seats * 100;
        }

        public override void ShowInfo()
        {
            base.ShowInfo();
            Console.WriteLine("Type: Car, Seats: " + seats);
        }
    }

    class Motorcycle : Vehicle
    {
        private int engineCC;

        public Motorcycle(string regNumber, string brand, int year, int engineCC)
            : base(regNumber, brand, year)
        {
            this.engineCC = engineCC;
        }

        public override double CalculateRental(int days)
        {
            return 500 * days;
        }

        public override void ShowInfo()
        {
            base.ShowInfo();
            Console.WriteLine("Type: Motorcycle, Engine: " + engineCC + " cc");
        }
    }

    class Truck : Vehicle
    {
        public Truck(string regNumber, string brand, int year)
            : base(regNumber, brand, year)
        {
        }

        public override double CalculateRental(int days)
        {
            return 3000 * days;
        }

        public override void ShowInfo()
        {
            base.ShowInfo();
            Console.WriteLine("Type: Truck");
        }
    }

    class HeavyTruck : Truck
    {
        private double loadCapacity;

        public double LoadCapacity
        {
            get { return loadCapacity; }
            set { loadCapacity = value; }
        }

        public HeavyTruck(string regNumber, string brand, int year, double loadCapacity)
            : base(regNumber, brand, year)
        {
            this.loadCapacity = loadCapacity;
        }

        public override double CalculateRental(int days)
        {
            return base.CalculateRental(days) + loadCapacity * 500 * days;
        }

        public override void ShowInfo()
        {
            base.ShowInfo();
            Console.WriteLine("Heavy truck, Load capacity: " + loadCapacity + " tons");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Vehicle[] vehicles = new Vehicle[4];
            vehicles[0] = new Car("DHA-1111", "Toyota", 2020, 5);
            vehicles[1] = new Motorcycle("DHA-2222", "Yamaha", 2022, 150);
            vehicles[2] = new Truck("DHA-3333", "Tata", 2018);
            vehicles[3] = new HeavyTruck("DHA-4444", "Volvo", 2021, 12.5);

            double[][] fuel = new double[4][];
            fuel[0] = new double[] { 6.5, 7.0, 6.8 };
            fuel[1] = new double[] { 2.1, 2.4 };
            fuel[2] = new double[] { 15.2, 14.8, 16.0, 15.5 };
            fuel[3] = new double[] { 25.0 };

            int days = 3;
            for (int i = 0; i < vehicles.Length; i++)
            {
                vehicles[i].ShowInfo();
                Console.WriteLine("Rental for " + days + " days: " + vehicles[i].CalculateRental(days));
                Console.Write("Fuel records: ");
                for (int j = 0; j < fuel[i].Length; j++)
                {
                    Console.Write(fuel[i][j] + " ");
                }
                Console.WriteLine();
                Console.WriteLine();
            }

            Console.WriteLine("--- Typecasting ---");
            Vehicle v = new HeavyTruck("DHA-5555", "Hino", 2023, 8);
            Console.WriteLine("Upcast (Vehicle reference) rental for 1 day: " + v.CalculateRental(1));

            if (v is HeavyTruck)
            {
                HeavyTruck h = (HeavyTruck)v;
                Console.WriteLine("Downcast (HeavyTruck reference) load: " + h.LoadCapacity + " tons");
            }

            Truck t = (Truck)v;
            Console.WriteLine("Truck reference brand: " + t.Brand);

            Console.ReadLine();
        }
    }
}
