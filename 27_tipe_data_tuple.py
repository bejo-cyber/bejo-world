# list
ganjil = [1,3,5,7,9]

# tuple
genap = (2,4,6,8,10)

print(type(ganjil))
print(type(genap))

ganjil[2] = 99
ganjil.append(2)
ganjil.remove(9)
print(ganjil)

# list bisa menggunakan [], append, remove. sedangkan tuple tidak bisa
# kita bisa mengecek dengan menggunakan dir
print('================dir(list)')
print(dir(ganjil))
print('================dir(tuple)')
print(dir(genap))


print('1==========================')
# tuple hanya bisa count dan index
genap = (2,4,6,6,8,10)

print(genap.count(6))
print(genap.index(8))

print('2==========================')

import sys
data_list = [1,2,3,4,5,'pisang goreng','syahrini','via vallen',False,3,14]
data_tuple = (1,2,3,4,5,'pisang goreng','syahrini','via vallen',False,3,14)

print('data list: ',data_list)
print('data tuple: ',data_tuple)

print('3==========================')
besar_data_list = sys.getsizeof(data_list)
besar_data_tuple = sys.getsizeof(data_tuple)

print('besar data list: ',besar_data_list)
print('besar data tuple: ',besar_data_tuple)

print('4==========================')

import timeit
data_list = timeit.timeit(stmt='[1,2,3,4,5,6,7,8,9]',number=1000000)
data_tuple = timeit.timeit(stmt='(1,2,3,4,5,6,7,8,9)',number=1000000)
print('waktu untuk memproses data list: ',data_list)
print('wakyu untuk memproses data tuple: ',data_tuple)






