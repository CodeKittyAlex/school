# kirjuta programm mis
# küsib kasutajalt kui suur ta põrand on
# (selle jaoks on vaja ristküliku valemit kasutada, ning küsida kasutajalt a ja b külg sentimeetrites)
# küsib kasutajalt milliseid põrandaplaate ta tahab
# kasutajale antakse 6 ascii näidet, ja kasutaja sisestab numbri milline muster talle meeldib
#
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄ (muid mustreid saab välja mõelda kas tähtedest või start -> character map abiga)
# (ülejäänud kolm mustrit mõtle ise)
# väljasta kasutajale ekraan mustriga koos hinnaarvutusega.
# (esimene muster on odavaim, viimane kalleim, tehe on pindala*mustriväärtus)
# küsi kas kasutaja maksab või mitte
# kui ei maksa, alanda hinda 10% ja küsi uuesti
# kui ei maksa, alanda hinda veel samapalju ja ütle viimane hind

a = int(input('how long be ye floor (cm)'))
b = int(input('how wide be ye floor (cm)'))
zafloo = a * b
print('what type of flooring would ye like')
#15
print('1')
print('1.5 eur')
print('██░░')
print('░░██')
print('2')
print('2.0 eur')
print('║┌─┐')
print('║└─┘')
print('3')
print('2.2 eur')
print('▀▄░░')
print('░░▀▄')
print('4')
print('3.0 eur')
print('▀▄▀▄')
print('▀▄▀▄')
print('5')
print('2.3 eur')
print('░░░░')
print('░░░░')
print('6')
print('1.8 eur')
print('██░░')
print('██░░')
flochoice = int(input('what floor will you be buying?'))
if(flochoice == 1):
    print('██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░')
    print('░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██')
    print('██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░')
    print('░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██')
elif(flochoice == 2):
    print('║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐')
    print('║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘')
    print('║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐║┌─┐')
    print('║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘║└─┘')
elif(flochoice == 3):
    print('▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░')
    print('░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄')
    print('▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░')
    print('░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄░░▀▄')
elif(flochoice == 4):
    print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄')
    print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄')
    print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄')
    print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄')
elif(flochoice == 5):
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
elif(flochoice == 6):
    print('██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░')
    print('██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░')
    print('██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░')
    print('██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░██░░')
if(flochoice == 1):
    floamount = zafloo *1.5
elif(flochoice == 2):
    floamount = zafloo *2.0
elif (flochoice == 3):
    floamount = zafloo *2.2
elif (flochoice == 4):
    floamount = zafloo *3.0
elif (flochoice == 5):
    floamount = zafloo * 2.3
elif (flochoice == 6):
    floamount = zafloo * 1.8
aw = input(f'will you be paying {floamount} euros yes/no')
if (aw.lower() == 'no'):
    tenof = floamount /100*10
    floamount = floamount-tenof
    aw2 = input(f'will you be paying {floamount} euros yes/no')
    if(aw2.lower() == 'no'):
        tenof = floamount / 100 * 10
        floamount = floamount - tenof
        aw3 = input(f'final offer: {floamount} euros yes/no')
        if (aw3.lower() == 'no'):
            print("sad we couldn't find even ground")
        elif(aw3.lower() == 'yes'):
            print('pleasure doing bussines with you')
        else:
            print("err")
    elif(aw2.lower == 'yes'):
        print('pleasure doing bussines with you')
    else:
        print('err')
elif(aw.lower == 'yes'):
    print('pleasure doing bussines with you')
else:
    print('err')
