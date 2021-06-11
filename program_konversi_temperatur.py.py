print('====PROGRAM KONVERSI TEMPERATUR====')
print('1. Celcius')
print('2. Reamour')
print('3. Fahrenheit')
print('4. Kelvin')

x = int(input('Pilihlah opsi berikut: '))

if x == 1:
    C = float(input('Masukan suhu dalam Celcius:'))
    R = (4/5)*C
    F = (9/5)*C+32
    K = C+273
    
    print('Suhu dalam Celcius: ',C,'C')
    print('Suhu dalam Reamour: ',R,'R')
    print('Suhu dalam Fahrenheit: ',F,'F')
    print('Suhu dalam Kelvin: ',K,'K')
elif x == 2:
    R = float(input('Masukan suhu dalam Reamour:'))
    C = (5/4)*R
    F = (9/4)*R+32
    K = (5/4)*R+273
    
    print('Suhu dalam Reamour: ',R,'R')
    print('Suhu dalam Celcius: ',C,'C')
    print('Suhu dalam Fahrenheit: ',F,'F')
    print('Suhu dalam Kelvin: ',K,'K')
elif x == 3:
    F = float(input('Masukan suhu dalam Fahrenheit:'))
    C = 5/9*(F-32)
    R = 4/9*(F-32)
    K = 5/9*(F-32)+273
    
    print('Suhu dalam Fahrenheit: ',F,'F')
    print('Suhu dalam Reamour: ',R,'R')
    print('Suhu dalam Celcius: ',C,'C')
    print('Suhu dalam Kelvin: ',K,'K')
elif x == 4:
    K = float(input('Masukan suhu dalam Kelvin:'))
    C = K-273
    R = 4/5*(K-273)
    F = 9/5*(K-273)+32
    
    print('Suhu dalam Kelvin: ',K,'K')
    print('Suhu dalam Fahrenheit: ',F,'F')
    print('Suhu dalam Reamour: ',R,'R')
    print('Suhu dalam Celcius: ',C,'C')
    
else:
    print('Pilihan yang anda masukan salah')
    
    
    





