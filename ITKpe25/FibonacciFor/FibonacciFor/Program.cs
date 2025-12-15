namespace FibonacciFor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("\n\n");
            Console.Write("Näita esimest Fibonacci seeriat");
            Console.WriteLine("--------------------------------\n\n");
            Console.WriteLine("sisesta number");
            int prv = 0, pre = 1, trm, n;
            n = Convert.ToInt32(Console.ReadLine());

            Console.Write($"siin on Fibonacci seeria{0} kuni \n", n);

            Console.Write($"{0} {1}", prv, pre);
            Console.Write("\n\n");

            for (int i = 3; i <= n; i++)
            {
                trm = prv + pre;   
                Console.WriteLine(trm);
                prv = pre;
                pre = trm;
                
            }
        }
    }
}
