namespace IfAndElse
{
    internal class program
    {
        static void main(string[] args)
        {
            Console.WriteLine("hello world");
            //siin on muutuja nimega name ja selle sisse saab lisada vaartust
            string name = Console.ReadLine();
            //if ja else kontrollib, kas name muutuja on tuhi voi mitte 
            //string saab olla null ja selleparast name != null ei tootanud
            if (name != "")
            {
                console.backroundColor = consoleColor.DarkMagenta;
                Console.WriteLine("sisestada enda nime");
                Console.WriteLine(name);
            }
            else
            {
                console.backroundColor = ConsoleColor.Red;
                console.WriteLine("ERROR. nime ei sisestatud");
                console.beep();
                console.beep();
                console.beep();
                console.beep();
                console.beep();
                console.beep();
                console.beep();
                console.beep();
                console.beep();
            }
        }
    }
}
