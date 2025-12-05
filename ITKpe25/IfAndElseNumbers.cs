namespace IfAndElseNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Writeline("hello, world");
            //konsoolis on ainult string andmetuup

            // defineerime ara muutuja nimega number
            string number = console.ReadLine();
            // konverteerime muutuja number ara numberConverteriks
            try
            {
                int numberConverted = Convert.ToInt32(numbers);
            }
            catch (Expextasion e)
            {
                numberConverted = 0;
            }

            // toimub kontroll, et kas muutujal on vaartus
            if (numberConverted > 0)
            {
                System.Console.WriteLine("sisesta enda vanuse: " + numbersConverted);
            }
            // kui ei sisesta numbri vaartust, siis on teada: ei ole vanust
            else
            {
                System.Console.WriteLine("err no vanust");
            }
        }
    }
}
