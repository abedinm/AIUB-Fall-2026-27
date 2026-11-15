using System;


class Program
{
    static void Main()
    {
        namespace M1
        {
            public class One
            {
                private protected string m;
                public const double n;
                internal byte o;
                protected internal byte p;
            }

            public class Two : One
            {
                public readonly byte i = 9;
                public void M() { }
            }

            class Program : Two
            {
                static void Main(string[] args)
                {
                    One obj1 = new One();
                }
            }
        }

        namespace M2   // Here, M2 has a reference of M1 (another assembly)
        {
            class Three
            {
                internal string a;
                internal Three() { }
                internal Three(byte i) { }
                internal Three(char d) { }
            }

            public class Four : M1.One
            {
                string p1;
                protected int q1;
                public void F1() { }
            }

            class Program : Four
            {
                public void F2(params int[] y)
                {
                    Three obj2 = new Three();
                }
            }
        }
    }
}