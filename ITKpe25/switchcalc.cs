namespace switchCalculator
{
    internal class program
    {
        static void main(string[] args)
        {
            Console.WriteLine("sisesta esimene number");
            unonum = float.parse(console.ReadLine());
            Console.WriteLine("sisesta teine number");
            tosnum = float.parse(console.ReadLine());
            Console.WriteLine("+ - /  *");
            valik = Console.ReadLine();

            switch (valik)
            {
                case "+":
                    awnser = unonum + tosnum;
                case "-":
                    awnser = unonum - tosnum;
                case "/":
                    awnser = unonum / tosnum;
                case "*":
                    awnser = unonum * tosnum;
                default:
                    Console.WriteLine("err");
            }
            Console.WriteLine(awnser);
        }
    }

}
