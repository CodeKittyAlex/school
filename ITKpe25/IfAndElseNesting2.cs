namespace intro
{
    internal class Program
    {
        // 
        static void Main(string[] args)
        {
            Console.Writeline("teha uks if ja else nestimine iseseisvalt");
            Console.WriteLine("teise else if-i sisse panna if ja else nestimine");

            if (y == 12)
            {
                System.Console.WriteLine("y vordub 12");
            }
            else if (y > 20)
            {
                if (y == 25)
                {
                    System.Console.WriteLine("Y vordub 25");
                }
                else
                {
                    System.Console.WriteLine("y on vahemikus 21 kuni 24 ja 26 kuni lopmatuseni");
                }
            }
            else
            {
                System.Console.WriteLine("mingi kahtlasen numbrid jalle");
            }
        } 
    }
}