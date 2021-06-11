# for loop


print('1======================')
# list sebagai iterable
pai_c = ['bagas','nasrul','hamam','amin','danang','andi']
for g in pai_c:
    print(g)
    print(len(g))

print('2======================')
# string sebagai iterable
bagas = 'bagas'
for i in bagas:
    print(i)

print('3======================')
# for di dalam for
buah = ['semangka','mangga','anggur','jeruk','apel']
sayur = ['kangkung','wortel','bayam','kentang','tomat']
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','pisang goreng']
daftar_belanja = [buah,sayur,gorengan]
for sub_daftar_belanja in daftar_belanja:
    print(sub_daftar_belanja)
    for komponen in sub_daftar_belanja:
        print(komponen)