# teknik loping

nama_band = ['payung teduh',
             'fourtwnty',
             'dialog dini hari',
             'mr. sonjaya',
             'parahyena']
iterasi = 1
for band in nama_band:
    print('no:',iterasi,'nama band',band)
    iterasi +=1

print('1=======================')

nama_band = ['payung teduh',
             'fourtwnty',
             'dialog dini hari',
             'mr. sonjaya',
             'parahyena']

lagu = ['akad',
        'zona nyaman',
        'rumahku',
        'sang filsuf',
        'sindara']

print('2=======================')
# enumerate

for i,band in enumerate(nama_band):
    print(i,':',band)

print('3=======================')
# zip

for band,lagu in zip(nama_band,lagu):
    print(band,'menyanyikan lagu',lagu)
  
print('4=======================')
# set  
play_list = {'baby baby','ada apa dengan cinta','cenat cenut', 'jaran goyang','jaran goyang','gorgon','kuda'}
for lagu in sorted(play_list):
    print(lagu)
    
print('keys=======================')
# dictionary
play_list2 = {'payung teduh':'akad',
             'fourtwnty':'zona nyaman',
             'dialog dini hari':'rumahku',
             'mr. sonjaya':'sang filsuf',
             'parahyena':'sindara'}
for i in play_list2.keys():
    print(i)
print('values=======================')
for i in play_list2.values():
    print(i)
print('items=======================')
for i in play_list2.items():
    print(i)
print('items=======================')
for i,v in play_list2.items():
    print(i,'menyanyikan',v)
print('reversed=======================')
for i in reversed(range(1,10,1)):
    print(i)
    














    
    
    
    
    
    