namespace IfAndElseFlowCharts
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("hello, world");

            string muutuja = System.Console.WriteLine();

            if (muutuja == "")
            {
                System.Console.WriteLine("ei sisestanud nime");
            }
            else
            {
                System.Console.WriteLine("sisestasid nime " + muutuja);
            }
        }
    }
}