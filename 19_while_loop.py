# while

print('1=========================')
angka = 0
while angka < 5:
    print('nilai angka adalah',angka)
    angka += 1 # jika tidak ditambah 1 maka akan terus menge-print tanpa henti
print('di luar while')

print('2=========================')
start= True
angka = 0
while start:
    print('di dalam while')
    if angka is 100:
        start = False
        print('angka 100 ditemukan')
    angka += 1

print('3=========================')
angka = 0
while angka < 5:
    print('nilai angka adalah',angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah',angka)

print('4=========================')
angka = 0
while angka < 10:
    if angka is 5:
        #print('checkpoint 1')
        continue
        break
        pass
        #print('checkpoint 2')
    print('nilai angka adalah',angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah',angka)
print('di luar while')


