namespace NameControllIfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            Console.WriteLine("what be thy name");
            string name = Console.ReadLine();

            if (name == "")
            {
                Console.BackgroundColor = ConsoleColor.White;
                Console.ForegroundColor = ConsoleColor.Green;
                Console.Beep();
                Thread.Sleep(2000);
                Console.Beep();
                Thread.Sleep(2000);
                Console.Beep();
                Thread.Sleep(2000);
                Console.WriteLine("name wasn't entered");
            }
            else
            {
                Console.BackgroundColor = ConsoleColor.Green;
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("hello " + name);
            }
        }
    }
}
