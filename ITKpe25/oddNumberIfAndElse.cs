namespace datatipes
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.Writeline("sisesta number");
            int number = convert.ToInt32(Console.ReadLine());

            if (number %2 == 0)
            {
                System.Console.WriteLine("even");
            }
            else
            {
                System.Console.WriteLine("odd");
            }
        }
    }
}