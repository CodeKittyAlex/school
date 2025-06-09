# 1 - kasutajatuvastus biomeetriaga: kirjuta programm mis:
#
# küsib kasutajalt tema kasutajanime ja parooli.
# - tsükkel kontrollib et mõlemad oleksid õiged
# - tsükkel toimib niikaua kuni üks kahest on vale
# - kasutajal on 3 katset sisselogimiseks
# - - kui kasutaja on sisestanud õige kasutajanime ja parooli,
# - - küsitakse tsükliga kuuekohalist 2FA arvkoodi.
# - - programm ei pea teadma kas 2FA kood on õige või mitte,
# - - peab kontrollima ainult et arv on kuuekohaline, ja et andmetüüp oleks täisarv (mitte sellises järjestuses)
# - - kui kood on vale, siis küsitakse kasutajalt kas ta tahab tuvastada ennast näo abil
# - - - tsükli sees teine tsükkel küsib kasutajalt küsimusi:
# - - - - mis kujuga ta nägu on, kas ovaalne, kandiline või piklik.
# - - - - mis värvi ta silmad on, kas pruunid, sinised või rohelised.
# - - - - mis värvi ta juuksed on, kas pruunid, blondid või oranzid.
# - - - - tsükkel küsib niikaua kuni kasutaja kirjutab küsimuste vastused õigel kujul
# - - - - - kasutajal on kindel välimus, a ja b ja c. milline täpsemalt, otsustate teie, muudel puhul ütleb et tuvastus ei õnnestunud
#
#

name = ''
code = 0
i = 0
test = 0
while (test == 0):
    name = input('what be ye name')
    code = int(input('what be the code'))
    print(name)
    print(code)
    if (name.lower() == 'alex') & (int(code) == 420):
        print('test')
        test =+1
        break
    i =+1
    if (i == 3):
        print('you have used up 3 trys')
        quit()

while (test == 1):
    tfa = int(input('what be ye 2fa'))
    if(tfa.len() == 6 ):
        print('welcome')
        quit()
    else:
        q = input('do you wish do use thy face')
        while(q.lower() == 'yes'):
            shape = input('what be ye head shape (ovaalne, kandiline või piklik)')
            eyecolor = input('what be ye eye color (ruunid, sinised või rohelised)')
            hair = input('what be ye hair color (pruunid, blondid või oranzid)')
            if (shape.lower() == 'ovaalne') & (eyecolor.lower() == 'sinine') & (hair.lower() == 'blondid'):
                print('welcome')
                quit()