namespace switchCoulors
{
    internal class program
    {
        static void Main(string[] args)
        {
            console.WriteLine("sisesta vokaal ja vajuta enter");
            color color = (color)(new random()).next(0.5);

            switch (input)
            {
                case color.red:
                    Console.backroundColor(red);
                    break;

                case color.green:
                    Console.backroundColor(green);
                    break;

                case color.blue:
                    Console.backroundColor(blue);
                    break;

                case color.white:
                    Console.backroundColor(white);
                    break;

                case color.orange:
                    Console.backroundColor(orange);
                    break;

                default:
                    System.Console.WriteLine("err");
                    break;
            }
        }
        public enum color
            {
                red, 
                green,
                orange,
                white,
                blue
            }
    }
}
 