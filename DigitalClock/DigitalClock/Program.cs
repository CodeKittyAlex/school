
namespace DigitalClock
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Digital clock";
            Console.CursorVisible = false;

            //tsükli algus point
            //while (true)
            //{
                 //tühjendab konsooli akne
                //Console.Clear();
                 //muutuja millel on arvuti aeg
                //string time = DateTime.Now.ToString("HH:mm:ss");

                 //leiab laiuse keskpunkti kus näidata aega
                //int x = (Console.WindowWidth - time.Length) / 2;
                 //leiab kõrguse keskpunkti kus näidata aega
                //int y = Console.WindowHeight / 2;

                 //sättib kella positsiooni
                //Console.SetCursorPosition(x, y);
                 //näitab aega
                //Console.Write(time);
                 //ootab 1sec
                //Thread.Sleep(1000);
            //}
            //for loopiga teha
            int num = int.Parse(Console.ReadLine());
            for (int i = 0; i < 8; i++)
            {
                Console.Clear();
                string time = DateTime.Now.ToString("HH:mm:ss");

                int x = (Console.WindowWidth - time.Length) / 2;
                int y = Console.WindowHeight / 2;

                Console.SetCursorPosition(x, y);
                Console.Write(time);
                
                Thread.Sleep(1000);
            }





        }
    }
}
