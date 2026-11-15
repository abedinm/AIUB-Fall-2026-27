using System;


class Program
{
    static void Main()
    {
        namespace Shop
        {
            public class Item
            {
                private int code;
                protected string label;
                internal double price;
                protected internal int stock;
                private protected bool onSale;
                public const int MaxStock = 500;
                public readonly string brand = "AIUB";

                public Item() { }
                public Item(string label) { this.label = label; }
                public Item(string label, double price) { this.label = label; this.price = price; }

                public virtual void Show() { }
                public void Restock(ref int amount) { }
            }

            public class Phone : Item
            {
                public override void Show() { }
                public void Discount(params double[] rates) { }
            }

            class Program
            {
                static void Main(string[] args)
                {
                    Item it = new Item("Pen");
                    Phone ph = new Phone();
                }
            }
        }

        namespace Online   // Online is another assembly that has a reference to Shop
        {
            class Tablet : Shop.Item
            {
                public void Check() { }
            }
        }
    }
}