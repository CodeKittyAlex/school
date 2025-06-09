
name = ''
long = ''
wide = ''
tall = ''
tr1 = True
tr2 = True
tr3 = True
tr4 = True
country = ''



while (name == ''):
    name = input('what be ye name')
    if (len(name) >= 25):
        print('max len reached cant go over 25')
        name = ''
while (tr1 ==True) or (tr2 == True) or (tr3 == True) or (tr4 == True):
    long = int(input('how long be ye(cm)'))
    if (long != 0):
        tr1 = False
        print('test')
    wide = int(input('how wide be ye'))
    if(wide != 0):
        tr2 = False
    tall = int(input('how tall be ye'))
    if (tall != 0):
        tr3 = False
    zaheavy = int(input('how heavy be ye'))
    if (zaheavy != 0):
        tr4 = False
while (country == ''):
    country = input('what be ye country of orygin')
    if (len(country) >= 25):
        print('max len reached cant go over 25')
        country = ''