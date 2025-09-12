namespace IfAndElseNesting
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("if and else nesting");

            // muutuja nimega y on andmetuup double e komagohaga anv ja vaartus on 9
            double y = 9;

            // sulgude sees olevat vaartust kontrollitakse, et kas vastab toene voi mitte
            if (y == 9)
            {
                // kui ma pannen if-i sisse if-i siis seda nimetatakse nestimiseks
                if (y == 11)
                {
                    System.Console.WriteLine("vastus on 11");
                }
                else
                {
                    System.Console.WriteLine("vastus oli 0 kuni 10 ja 12 kuni 19");
                }
            }
            else if (y == 20.5)
            {
                System.Console.WriteLine("vastus on 20.5. teine tingimus vastab toele");
            }
            else if (y == 30)
            {
                System.Console.WriteLine("vastus on 30. kolmas tingimus vastab toele");
            }
            else
            {
                System.Console.WriteLine("mingi kahtlane number");
            }
        }
    }
}