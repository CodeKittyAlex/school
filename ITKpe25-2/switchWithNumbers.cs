namespace switchWithNumbers
{
    internal class program
    {
        static void main(string[] args)
        {
            System.Console.WriteLine("genereerib numbreid 1-6");

            switch (num)
            {
                case "1":
                    Console.beep(1000, 500);
                    break;

                case "2":
                    Console.beep(2000, 500);
                    Console.beep(2000, 500);
                    break;

                case "3":
                    Console.beep(3000, 500);
                    Console.beep(3000, 500);
                    Console.beep(3000, 500);
                    break;

                default:
                    System.Console.WriteLine("err");
                    break;
            }
        }
    }
}