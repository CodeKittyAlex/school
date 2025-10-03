
namespace MethodCallIfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("hello, world");
            string anw = System.Console.ReadLine();
            if (anw == "yes")
            {
                Console.WriteLine();
            }
            else if (anw == "no")
            {
                Console.WriteLine();
            }
            else
            {
                Console.WriteLine("err");
            }
            //siin kutsun do something meetodit
            doSomething()
        }
        static void doSomething()
        {
            System.Console.WriteLine("does something");
        }
    }
}