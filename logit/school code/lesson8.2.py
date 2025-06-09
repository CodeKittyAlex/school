
aw1 = input('kas teil on hapukapsast (jah/ei)')
aw2 = input('kas teil on pott (jah/ei)')
aw3 = input('kas teil on vett(jah/ei)')
aw4 = input('kas teil on kartulid(jah/ei)')
aw5 = input('kas teil on puljongit(jah/ei)')

if(aw1.lower() == 'jah') & (aw2.lower() == 'jah') & (aw3.lower() == 'jah') & (aw4.lower() == 'jah') & (aw5.lower() == 'jah'):
    print('ühepajatoitu saab teha')
if(aw1.lower() == 'ei'):
    print('hautist saab teha')
if(aw2.lower() == 'ei'):
    print('suppi ei saa teha')
if(aw3.lower() == 'ei'):
    print('mulgikapsast saab teha')
