namespace IfAndElseFootNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("hello, world");

            System.Console.WriteLine("what be thy foot size");
            int(size = Console.ReadLine());

            if (size >= 30 && size <= 33)
            {
                Console.ForegroundColor = ConsoleColor.Green
                Console.Writeline("size 30-33")
            }
            else if (size >= 34 && size <= 38)
            {
                Console.ForegroundColor = ConsoleColor.White
                Console.Writeline("size 34-38")
            }
            else if (size >= 39 && size <= 44)
            {
                Console.ForegroundColor = ConsoleColor.Yellow
                Console.Writeline("size 39-44")
            }
            else if (size >= 45 && size <= 48)
            {
                Console.beep
                Console.Writeline("size 45-48")                
            }
            else
            {
                Console.Writeline("a valid size was not entered")
            }
        }
    }
}
