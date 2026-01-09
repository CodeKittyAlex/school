namespace rectangle
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            int a = int.Parse(Console.ReadLine());
            int b = int.Parse(Console.ReadLine());

            for (int i = 0; i < a; i++)
            {
                for (int j = 0; j < b; j++)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }
            int pindala = a * b;
            int ümbermõõt = (a + b) * 2;
            Console.WriteLine($"ristküliku pindala on {pindala} ja ümbermõõt on {ümbermõõt}");
        }
    }
}
