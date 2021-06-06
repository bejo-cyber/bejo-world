#INPUT USER

#apapun yang dimasukkan pasti berupa data string
data = input('masukan data: ')
print("data = ",data,"type = ", type(data))

#jika ingin mengambil data int, maka
angka1 = float(input('masukan angka: '))
angka2 = int(input('masukan angka: '))
print("data = ",angka1, 'type = ',type(angka1))
print("data = ",angka2, 'type = ',type(angka2))

#bolean
biner = bool(int(input('masukan nilai boolean: ')))
print('data = ',biner,'type = ', type(biner))