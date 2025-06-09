#külje leidmine
print("first gube size")
A = int(input())
print("second gube size")
B = int(input())

#ruumala leidmine
ruumala1 = A ** 3
ruumala2 = B ** 3

#ruumala kokku
ruumala = (ruumala1 + ruumala2)

#teatamine
print('teil on vaja kuubi mille ruumaal on minimaalselt' ,ruumala)

#leia kasti suurus
print("kui suur on kast kuupsentimeetrites")
cubesize = int(input())
mark = 100
mark_vajadus = cubesize / mark
print("teil on vaja",mark_vajadus ,"marki")
print("kas teil on piisavalt marke")
print("y/n")
awnser = str.lower(input())
if awnser == "y":
    print("pakk on teelepandud")
else:
    print("kahjuks ei saa pakki saata")





