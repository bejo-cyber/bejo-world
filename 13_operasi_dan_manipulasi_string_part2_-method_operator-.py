# operator dalam bentuk method

## merubah case dari string

#merubah semua ke upper case

salam = 'bro!'
print('normal : ', salam)
salam_up = salam.upper()
print('upper : ', salam_up)

# merubah seua ke lower case
alay = 'aKu KeCe AbiiieeeezzZZzZZ'
print('normal : ', alay)
alay_low = alay.lower()
print('lower : ',alay_low)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = 'sist!'
apakah_lower = salam.islower() # hasilnya adalah boolean
print(salam, 'is lower : ',str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya adalah boolean
print(salam, 'is upper : ',str(apakah_upper))

# isalpha() -> untuk mengecek semuanya huruf
# isalnum() -> huruf dan angka
# isdecimal() -> angka saja
# isspace() -> spasi, tab, newline \n
# istitle() -> semua kata dimulai dengan huruf besar

judul = 'It Is Okay Not To Be Orkay'
cek_judul = judul.istitle() # hasilnya pasti boolean
print(judul,' is title : ',str(cek_judul))

## ngecek komponen startwith() endwith
cek_start = 'Sangjanim Oppa'.startswith('Sangjanim')
print('start :',str(cek_start))

cek_end = 'Sangjanim Oppa'.endswith('Sangjanim Oppa')
print('end : ',str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)


gabung = 'akuehmsayangehmkamu'
print(gabung.split('ehm'))

# alokasi karakter rjust() ljust() center()

kanan = 'kanan'.rjust(10)
print(5*'='+kanan+'='*5)

kiri = 'kiri'.ljust(10)
print(5*'='+kiri+'='*5)

center = 'center'.center(10)
print(5*'='+center+'='*5)

center = 'center'.center(20,'x')
print(5*'='+center+'='*5)

center = 'center'.center(20,'^')
print(5*'='+center+'='*5)

# kebalikannya -> strip()
tengah = center.strip('^')
print(5*'='+tengah+'='*5)
