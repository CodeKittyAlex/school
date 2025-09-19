namespace brackets
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("hello, brackets");

            System.Console.WriteLine("kui palju on 3 + 8 /(4 - 2) * 4");

            // arvuti arvutab: jagamine ja korrutamine on samal tasemel aga jagamine
            // oli seekord eespool. Alguses jagati 8 sulgudes olevat vaartusega, nis
            // tahendas 8 jagatud 2. jargnevalt korrutati see tulemus 4-ga ja saadi 16.
            // peale seda 16 liideti 3-ga ja saadi vastuseks 19.
            double calculation1 = 3 + 8 / (4 - 2) * 4;
            // antud juhul ei aksepteeri komakohaga numbrit
            double calculation2 = (3 + 8) / (4 - 2) * 4;
            double calculation3 = 3.0 + 8.0 / (4.0 - 2.0) * 4.0;


            System.Console.WriteLine("vastus " + calculation1);
            System.Console.WriteLine("vastus " + calculation2);
            System.Console.WriteLine("vastus " + calculation3);
        }
    }
}