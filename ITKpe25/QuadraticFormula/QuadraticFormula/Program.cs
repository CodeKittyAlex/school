namespace QuadraticFormula
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("ruutvõrrand");

            //ax2 + bx + c = 0

            //sisesta a, b ja c väärtus
            //kasutaja peab saama sisestadxa neid väärtuseid
            Console.WriteLine("mis on a");
            double a = double.Parse(Console.ReadLine());

            Console.WriteLine("mis on b");
            double b = double.Parse(Console.ReadLine());

            Console.WriteLine("mis on c");
            double c = double.Parse(Console.ReadLine());

            double d = b * b - 4 * a * c;

            Console.WriteLine($"x1 = {(-b + Math.Sqrt(d)) /(2 * a) }, x2 = {(-b + Math.Sqrt(d)) / (2 * a)}");
            //https://stackoverflow.com/questions/20054034/quadratic-equation-formula
        }
    }
}