namespace testGeomeetrilisedKujud
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("vali kuju püramiid(a), ristkülik(b), ruutvõrrand(c)");
            string valik = Console.ReadLine();

            switch (valik)
            {
                case "a":
                    
                    Console.WriteLine();
                    int h = int.Parse(Console.ReadLine());
                    for (int k = 0; k < h; k++)
                    {
                        
                    }
                    break;
                case "b":
                    Console.WriteLine("mis on a suurus");
                    int x = int.Parse(Console.ReadLine());
                    Console.WriteLine("mis on b suurus");
                    int y = int.Parse(Console.ReadLine());
                    for (int i = 0; i < x; i++)
                    {
                        for (int j = 0; j < y; j++)
                        {
                            Console.Write("*");
                        }
                        Console.WriteLine();
                    }
                    break;
                case "c":
                    Console.WriteLine("mis on a");
                    double a = double.Parse(Console.ReadLine());

                    Console.WriteLine("mis on b");
                    double b = double.Parse(Console.ReadLine());

                    Console.WriteLine("mis on c");
                    double c = double.Parse(Console.ReadLine());
                    
                    double d = b * b - 4 * a * c;
                    
                    Console.WriteLine("vastuseks on: " + d);
                    break;
                default:
                    Console.WriteLine("err");
                    break;
            }
        }
    }
}