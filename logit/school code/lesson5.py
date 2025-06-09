# kirjuta programm mis
#
# küsib kasutajalt kas tal on kõht tühi.
# kui kasutaja vastab ei:
#---siis programm ütleb talle vastu tagasi "ootame teid jälle kui teil isu on"
# kui kasutaja vastab ja:
#---küsib programm kas ta tahab ise võileiva kokku panna, või lasta arvutil selle genereerida
#---kui kasutaja tahab ise kokku panna, siis:
#-------küsib programm temalt kas ta tahab ühepoolset võileiba või kahepoolset võileiba:
#-------küsib programm temalt kas ta tahab võileivale võid või majoneesi
#-------küsib programm temalt kas ta tahab kurki võileivale
#-------küsib programm temalt kas ta tahab tomatit võileivale
#-------küsib programm temalt kas ta tahab peekonit võileivale
#---kui kasutaja tahab suvaliselt kokku panna, siis genereeritakse talle 5 korda erinev võileiva osa järjest
#---programm koostab kasutajale ascii pildi erinevatest kihtidest mida kasutaja lisanud on või arvuti genereerinud on
#---, ja küsib temalt raha 1.50 + 0.75 iga lisatud kihi eest
#---kui kasutaja ei maksa, siis öeldakse talle "ootame teid jälle kui teil isu on ja raha ka"
#---kui kasutaja maksab, siis tagastatakse ascii võileib teatega "aitäh tellimuse eest, tulge jälle"
# sai - [ , ,, '' ']
# või ja majoneesi jaoks ei kuvata kihti, aga ta annab hinnas lihtsalt juurde
# kurk - ▄▄▄▄ ▄▄▄
#tomat - ( | ▌|██)
#bacon - "~-,._.,-~"~-,.

import random

money = 1.50
i = 0
ingreamount = 0
sai = "[ , ,, '' ']"
kurk = "▄▄▄▄ ▄▄▄"
tomat = "( | ▌|██)"
bacon = '"~-,._.,-~"~-,.'
või = ''
list = [sai, kurk, bacon, või]
q1 = input('be ye hungry')
if (q1.lower() == 'no'):
    print("ootame teid jälle kui teil isu on")
elif(q1.lower() == 'yes'):
    q2 = input('do ye wish to make the sandwich')
    if(q2.lower() == 'yes'):
        q3 = input('do you wish for a one sided sandwich or a two sided one')
        q4 = input('do you wish for mayo or butter or neather?')
        q5 = input('do you wish for some cucombers')
        q6 = input('do you wish for some tomatos')
        q7 = input('do you wish for some bacon')
        if (q3 == 'two sided'):
            print(sai)
            ingreamount = ingreamount + 1
        if(q4 == 'mayo'):
            ingreamount = ingreamount + 1
        elif(q4 == 'butter'):
            ingreamount = ingreamount + 1
        if(q5 == 'yes'):
            ingreamount = ingreamount + 1
            print(kurk)
        if (q6 == 'yes'):
            ingreamount = ingreamount + 1
            print(tomat)
        if(q7 == 'yes'):
            ingreamount = ingreamount + 1
            print(bacon)
        print(sai)
        while i < ingreamount:
            money = money + 0.75
            i += 1
        pay = int(input (f'please pay {money} amount of money 0/1'))
        if (pay == 1):
            print ('have a good day')
        elif(pay == 0):
            print("ootame teid jälle kui teil isu on ja raha ka")
        else:
            print("err")
    elif(q2.lower() == 'no'):
        ranum = random.randint(0,5)
        rando = random.choices(list, k = ranum )

        while i < ranum:
            money = money + 0.75
            i += 1
        pay = int(input(f'please pay {money} amount of money 0/1'))
        if (pay == 1):
            print('have a good day')
        elif (pay == 0):
            print("ootame teid jälle kui teil isu on ja raha ka")
        else:
            print("err")
        while i < ranum:
            ingre = rando[i]
            if (ingre == sai):
                print(sai)
            if (ingre == või):
                if (ingre == kurk):
                    print(kurk)
            if (ingre == tomat):
                print(tomat)
            if (ingre == bacon):
                print(bacon)
            i += 1


    else:
        print('err awnser not acseptable')
else:
    print('err awnser not acseptable')
