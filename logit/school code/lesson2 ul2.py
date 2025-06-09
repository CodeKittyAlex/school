# kirjuta püütoni programm mis:

# arvutab keskmise väärtuse
# ja ütleb kasutajale, et tema perekonna keskmine pikkus on <arvutatudpikkus>
# programm arvutab eraldi vanemate keskmise pikkuse,
# ja väljastab selle eraldi lausena "sinu vanemate keskmine pikkus on <vanematepikkus>
# programm arvutab eraldi ka sinu ja su venna/õe keskmise,
# ja väljastab ka selle eraldi lausena "aga sinu ja su vendade-õdede keskmine on <lastepikkus>


print("what be ye hight")
yo = int(input())
print("what be ye moms hight")
mom = int(input())
print("what be ye dads hight")
a = int(input())
print("what be ye comrade hight")
hoe = int(input())

avarage = (yo + mom + a + hoe) / 4

print(f"the avarage hight is {avarage}")



