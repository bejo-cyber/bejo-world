# list
 
data = [1,4,9,16,25,36,49,64]
print('data :',data)

# mengakses list
print('1===============================')
sub_data = data[3]
print('baris ke-4 :',sub_data)
sub_data = data[0]
print('baris ke-1 :',sub_data)
sub_data = data[-1]
print('baris ke-(-1) :',sub_data)

# memotong list
print('2===============================')
sub_data = data[0:4]
print('baris 1 sampai 4 :',sub_data)
sub_data = data[0:2]
print('baris 1 sampai 2 :',sub_data)
sub_data = data[2:6]
print('baris 3 sampai 6 :',sub_data)

# menambah list
print('3===============================')
data1 = [1,4,9,16,25,36,49,64]
data2 = [100,200,300,400,500,600,700,800]
data3 =  data1 + data2
print('data 1 : ',data1)
print('data 2 : ',data2)
print('gabungan data 1 dan data 2 :',data3)

# merubah content dari list
print('4===============================')
data2 = [100,200,300,400,500,600,700,800]
print('data : ',data2)
data2[3]=87
print('menambahkan 87 setelah baris ke-3 :','\n',data2)

data2 = [100,200,300,400,500,600,700,800]
a = data2[:]
a[3]=87
print(data2)

# merubah content list dengan menggunakan metode slicing
print('5===============================')
data2 = [100,200,300,400,500,600,700,800]
data2 [3:5] = [11,12]
print(data2)

# list dalam list
print('6===============================')
data1 = [1,4,9,16,25,36,49,64]
data2 = [100,200,300,400,500,600,700,800]
x = data1,data2
print(x)

# methods untuk list
print('7===============================')
data1.append(data2)
print(data1)
data1 = [1,4,9,16,25,36,49,64]
data1.append(30)
print(data1)

# mengakses list dalam multidimensial list
print('8===============================')
y = x[0]
print(y)
y = x[0][3]
print(y)
y = x[1]
print(y)
y = x[1][4]
print(y)

# function yg bisa digunakan kepada list
print('9===============================')
data1 = [1,4,9,16,25,36,49,64]
panjang_list = len(data1)
print(panjang_list)

 