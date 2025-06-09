namespace ifelseif
{


    internal class programm
    {
        static void main(string[] args)
        {
            console.writeline("hello world");

            console.writeline("kui palju on 3 + 8 / (4 - 2) * 4 = ?");

            double calculation1 = 3 + 8 / (4 - 2) *4;
            double calculation2 = (3 + 8) / (4 - 2) *4;
            double calculation3 = (3 + 8) / (4 - 2) *4;
            double calculation4 = ((3.0 + 8.0) / (4.0 - 2.0) *4.0);

            console.writeline("vastus: "+calculation1)
            console.writeline("vastus: "+calculation2)
            console.writeline("vastus: "+calculation3)
            console.writeline("vastus: "+calculation4)
        }
    }
}