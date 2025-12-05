namespace IfAndElseP2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("Teha if ja else konsooli rakendus kus kontrollitakse stringi abil varvi vastavust");

            System.Console.WriteLine("varvide valikus on : red blue green ja white");
            System.Console.WriteLine("peab kasitlema juhust, kus vastaja ei sisesta eelpool sisestatud varvi");
            System.Console.WriteLine("sisesta varv");

            coulor = System.Console.ReadLine();
            if (coulor == red)
            {
                System.Console.WriteLine("omg u pikked wed uwu");
            }
            else if (coulor == blue)
            {
                System.Console.WriteLine("why bwue uwu");
            }
            else if (coulor == green)
            {
                System.Console.WriteLine("green");
            }
            else if (coulor == white)
            {
                System.Console.WriteLine("white");
            }
            else
            {
                System.Console.WriteLine("err color not a valid option");
            }
            System.Console.WriteLine();
        }
    }
}