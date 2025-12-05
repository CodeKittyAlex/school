namespace IfAndElseEnterNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("sisesta numbrid 1, 2 voi 3");

            string nr = console.ReadLine();
            int number = int.parse(nr);

            if (number == 1)
            {
                System.Console.WriteLine("sisestasid numbri 1");
            }
            else if (number == 2)
            {
                System.Console.WriteLine("sisestasid numbri 2");
            }
            else if (number == 3)
            {
                System.Console.WriteLine("sisestasid numbri 3");
            }
            else
            {
                System.Console.WriteLine("katkine number. ERROR!!!!!!");
            }
        }
    }
}