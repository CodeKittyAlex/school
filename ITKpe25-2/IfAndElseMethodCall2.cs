namespace IfAndElseMethodCall2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("sisesta number");
            int number = convert.ToInt32(Console.ReadLine());
            
            if (number % 2 == 0)
            {
                EvenNumber();
            }
            else
            {
                OddNumber();
            }
        }
        static void EvenNumber()
        {
            Console.WriteLine("tegemist on paaris numbriga");
        }
        static void OddNumber()
        {
            Console.WriteLine("tegemist on paaritu numbriga");
        }
    }
}