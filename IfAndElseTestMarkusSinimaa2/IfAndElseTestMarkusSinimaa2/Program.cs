namespace IfAndElseTestMarkusSinimaa2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("what be ye height");
            string height = Console.ReadLine();
            int heightnr = int.Parse(height);

            if (heightnr >= 40 && heightnr <= 80)
            {
                Console.WriteLine("sa oled 40cm ja 80 cm vahel");
                Console.WriteLine("sinu pikkus on " + heightnr + "cm");
            }
            else if (heightnr >= 81 && heightnr <= 130)
            {
                Console.WriteLine("sa oled 81cm ja 130 cm vahel");
                Console.WriteLine("sinu pikkus on " + heightnr + "cm");
            }
            else if (heightnr >= 131 && heightnr <= 170)
            {
                Console.WriteLine("sa oled 131cm ja 170 cm vahel");
                Console.WriteLine("sinu pikkus on " + heightnr + "cm");
            }
            else if(heightnr >= 171)
            {
                Console.WriteLine("sinu pikkus on " + heightnr + "cm");
            }
            else
            {
                Console.WriteLine("err height not in the system");
            }
        }
    }
}