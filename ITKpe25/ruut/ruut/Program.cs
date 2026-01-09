namespace ruut
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("mis arvu sa soovid teha ruutu");
            //teha for loopiga ruut
            int ruut = int.Parse(Console.ReadLine());

            for (int i = 0; i < ruut; i++)
            {
                for (int j = 0; j < ruut; j++)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }
            // a * 4 / a * a
            int pindala = (ruut * ruut);
            int ümbermõõt = (ruut * 4);

            Console.WriteLine($"ruudu ümbermõõt on {ümbermõõt} ja pindala on {pindala}");
            
        }
    }
}
