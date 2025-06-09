# Kirjuta programm mis:
#
# küsib kasutajalt tema nime
# küsib kasutajalt pin koodi
# automaadi pin kood on 8888
# kui pin kood on vale, siis teavitame kasutajat et politsei on kutsutud
# kui pin kood on õige, kuvatakse kasutajale tema kontosaldo, ja küsitakse
# kui palju soovid välja võtta?"
# kui kasutaja sisestab komakohaga arvu, siis öeldakse talle et masin ei väljasta sente, paku mõni muu arv
# kui kasutaja sisestab arvu mis ei lõppe 0 ega 5-ga, siis öeldakse, et masinal ei ole väiksemaid kupüüre, kui viiene.
# kui kasutaja sisestab hoopis sõna ei, siis lõpeb programm teavitusega "Teie pank ootab teid homme, head päeva jätku"
# kui kastuaja sisestab sobiva arvu, teavitatakse talle emojiga, et võtnud välja kupüüri suuruses kasutajasisestus. [€_(arv)]

money = 120000
pinkood = 8888

name = input('what be thy name')
kood = int(input('what be thy code'))



if (pinkood == kood):
    print (f'welcome { name }')
    mony = int(input('how much will you be withdraving'))
    if (type(mony) == float):
        print('no can do no sents')
    #elif(type(mony) == str):
        #print('no can do no words')
    elif(money < mony):
        print('no can do too much molla')
    else:
        print(f'you have withdrawn {mony} amount')
        print(type(mony))

else:
    print('no luck police on the way')





