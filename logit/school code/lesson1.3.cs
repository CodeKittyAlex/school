namespace aroundearth
{
    internal class program
    {
        static void Main(string[] args)
        {
            //mittu 2 eur münti läheb ümber maa
            //maa ümbermõõt välja arvutada raadiuse abil
            double coinDiamater = 25.75;//mm
            double earthradius = 6378160000;//mm
            //2 pi r
            double earthsircumfus = 2* math.pi * earthradius

            double coinamount = earthsircumfus / coinDiamater
            console.writeline(coinamount)
        }
    }
}