barang = ['sepeda','tas','sepatu','sandal','baju','topi']
print(barang,len(barang))

print('1--------------------------------')

# beberapa method yang bisa digunakan untuk memanipulasi list

# method untuk menambah data ke dalam list (append, extend, insert)
barang.append('kaca mata') # "append" <- digunakan untuk menambah data di list
print(barang,len(barang))

print('2--------------------------------')

data = 'test'
for i in data:
    print(i)
    
print('3--------------------------------')

data = 'test'
print(data[1])

print('3--------------------------------')

# extend
barang = ['sepeda','tas','sepatu','sandal','baju','topi']
barang.extend('dompet')
print(barang)

print('3--------------------------------')

# insert
barang = ['sepeda','tas','sepatu','sandal','baju','topi']
barang.insert(3,'dompet')
print(barang)

print('4--------------------------------')
# method untuk menghitung anggota
barang = ['sepeda','tas','sepatu','sandal','baju','sepeda','topi']
print(barang)
jumlahSepeda = barang.count('sepeda')
print('jumlah sepeda adalah : ',jumlahSepeda)

print('4--------------------------------')
# meremove data (menghapus data)
barang.remove('sepeda')
print(barang)

print('5--------------------------------')
# reverse (membalik data)
barang.reverse()
print(barang)

print('6--------------------------------')
stuff = barang.copy()
stuff.append('gelas')
print(stuff)
print(barang)




