def jumlah(a,b):
    c = a+b
    return c
hasil = jumlah(4,5)
print(hasil)
print('============================')
# hal di atas bisa disingkat dengan lambda, caranya:
# membuat anonymous dengan lamda
kali = lambda argumen:print(argumen)
kali('test')

bagi = lambda a,b: a/b
hasil = bagi(9,3)
print(hasil)

print('============================')

jumlah = lambda a,b:a+b
hasil = jumlah(3,4)
print(hasil)

