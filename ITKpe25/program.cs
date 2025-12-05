namespace switc
{
    internal class program
    {
        static void Main(string[] args)
        {
            console.WriteLine("sisesta vokaal ja vajuta enter");
            string input = Console.readLine();

            switch (input)
            {
                case "a":
                    System.Console.WriteLine("vokaal a");
                    break;
                
                case "e":
                    System.Console.WriteLine("vokaal e");
                    break;

                case "i":
                    System.Console.WriteLine("vokaal i");
                    break;
                
                default:
                    System.Console.WriteLine("muu tähr");
                    break;
            }
        }
    }
}
 