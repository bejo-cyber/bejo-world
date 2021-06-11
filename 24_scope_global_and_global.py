# scope variable : local

namaKucing = 'jono'
def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('nama baru kucingku adalah',namaKucing)

rubahNamaKucing('bejo')
print('nama kucingku dulu',namaKucing)

print('1=================================')
# scope variable : global

namaKucing = 'jono'
def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('nama baru kucingku adalah',namaKucing)

rubahNamaKucing('bejo')
print('nama kucingku dulu',namaKucing)

print('2=================================')

namaKucing = 'jono'
makananKucing = 'tongkol'
def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('nama baru kucingku adalah',namaKucing)
def kasihMakanKucing(nama,makanan):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('sadam')
kasihMakanKucing('alex','ikan gurami')
print('nama kucing saya',namaKucing,'dan makanannya adalah',makananKucing)
     







