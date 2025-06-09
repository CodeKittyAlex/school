# 2 - stonksid
#
# kirjuta programm mis:
# küsib kasutajalt kui palju ta soovib investeerida
# küsib kasutajalt millise firma aktsiaid ta soovib: tesla, transferwise, twitter
# - kui kasutaja valib transferwise või tesla, otsustatakse kordaja juhuarvu ja tehte abil (arv vahemikus 1 ja 100, juhuarv jagatakse 1000ga ja sinna liidetakse 1 juurde)
# - kui kasutaja valib twitteri, on kordaja iga tsükkel -1.15
# programm hoiab meeles kui palju kasutaja alguses investeeris
# programm töötab viis tsüklit (1 tsükkel iga tööpäeva kohta) ja töönädala lõpus:
# - väljastab kasutajale kui palju ta teenis või kaotas
# - ning küsib kas ta soovib oma aktsiad maha müüa või jätkata
# - - kui kasutaja soovib jätkata, siis tsükkel töötasb veel ühe nädala
# - - kui aga firma aktsia langeb nulli, siis öeldakse et firma on pankrotis, ja sinu raha läinud


q1 = int(input('how much do the wish to invest'))
q2 = input('witch firma would you like to invest in: tesla, transferwise, twitter')