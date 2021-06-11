# fungsi dengan menggunakan argumen sederhana

def siswa(nama): # (nama) <- adalah argumen
    print('siswa ini bernama',nama)
siswa('andi')

print('1============================')
# fungsi dengan menggunakan keywords arguments

def guru(nama,pelajaran):
    print('guru ini bernama',nama)
    print('mengajari',pelajaran)
guru('mario','matematika')
guru(pelajaran='olahraga',nama='tunari')

print('2============================')
# fungsi dengan menggunakan default argument

def penjagaSekolah(nama,shift='siang',sifat= 'galak'):
    print('penjaga sekolah ini bernama',nama)
    print('shiftnya',shift)
    print('sifatnya',sifat)
penjagaSekolah('rowi')
penjagaSekolah('sahrul',shift='malam')
penjagaSekolah('asep',sifat='sabar')
