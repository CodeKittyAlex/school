
namespace datatipes
{ 
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.Writeline("hello, world");

            //bool  andmetuup toetab ainult true ja false
            bool check = true;
            bool negative = false;

            //string
            //string on tahemark
            //koike saab sisestada mis on klaviatuuril
            string mark = "123";
            string mark2 = "123";
            console.Writeline(mark + mark2);

            //int
            //teha kalkulatsioon, kus muutuja taisarv liidetakse
            //taisarv 2-ga
            // tulemus peab naitama konsoolis
            int taisarv = 123;
            console.Writeline(taisarv * 2);

            //byte max vaartus on 255
            //0 kasitleb arvuti meie mottes, kui uhte
            byte a = 255;

            //sbite saab kasitleda nii negatiivset kui ga positiivset
            //positiivsete vaartuses 8-biti ulatuses
            sbyte b = -128;

            //char on tahemark
            //  
            char ch = "a";
            char numberch = '1';
            //kui baned 5 ette (char) siis seda nimetatakse castimiseks
            char numberch1 = (char)2;

            //desimal
            // tuleb panna numbri jargi m ja annab teada, et tegemist on desimal andme tuubiga
            decimal desim = 2.1m;

            //double
            //komakohaga arv
            double doub = 12.4;

            //float
            //komakohaga arv mis tahab f tahte loppu
            float komakohagaarv = 4.564F;

            //long
            //saab negatiivseid ja positiivseid numbreid lisada
            //max -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
            long longnr = -78723496981364;

            //short
            //16 byte arv
            short lyhikeAr = 20;
        }
    }
}
 