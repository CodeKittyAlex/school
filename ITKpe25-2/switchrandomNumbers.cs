namespace switchRandomNumber
{
    internal class program
    {
        static void main(string[] args)
        {
            System.Console.WriteLine("genereerib numbreid 1-6");
            Random rnd = new Random();
            int num = rnd.Next(1,7);

            switch (num)
            {
                case "1":
                    System.Console.WriteLine("1");
                    break;

                case "2":
                    System.Console.WriteLine("2");
                    break;

                case "3":
                    System.Console.WriteLine("3");
                    break;

                case "4":
                    System.Console.WriteLine("4");
                    break;

                case "5":
                    System.Console.WriteLine("5");
                    break;

                case "6":
                    System.Console.WriteLine("6");
                    break;

                default:
                    System.Console.WriteLine("err");
                    break;
            }
        }
    }
}