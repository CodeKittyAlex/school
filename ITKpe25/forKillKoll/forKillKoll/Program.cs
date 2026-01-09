namespace forKillKoll
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("sisesta arv");
            int arv = Convert.ToInt32 (Console.ReadLine());
            arv = arv + 1;

            for (int i = 1; i < arv; i++)
            {
                if (i % 3 == 0) 
                {
                    Console.WriteLine("killadi - koll");
                }
                else
                {
                    Console.WriteLine("kill - koll");
                }
                
            }
        }
    }
}
