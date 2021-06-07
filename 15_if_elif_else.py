
print("1======================")
nilai = 40

if nilai < 50: # jika nilai kurang dari 50 maka:
    print('anda remidi')
    
print("2======================")
nilai = 60

if nilai < 50: # jika nilai kurang dari 50 maka:
    print('anda remidi')# tidak akan keluar
print('kosong')
    
    
print("3======================")
nilai1 = 40
nilai2 = 11
if nilai1 < 50: # jika nilai kurang dari 50 maka:
    print('anda remidi')
    print('step 1')
    if nilai2 < 50: # jika nilai kurang dari 50 maka:
        print('anda remidi')
        print('step 2')
print("4======================")
nilai = 40
if nilai is 40:
    print('nilai anda :',nilai)
    
nilai = 40
if nilai is not 30:
    print('nilai anda bukan :',30)
    
print("5======================")
nilai = 70
if 80 <= nilai <= 100:
    print('nilai anda adalah A')
elif 70 <= nilai <= 80:
    print('nilai anda adalah B')
elif 50 <= nilai <= 70:
    print('nilai anda adalah C')
elif 30 <= nilai <= 50:
    print('nilai anda adalah D, lakukan remidi')
else:
    print('maaf anda tidak lulus')
    
print("6======================")
PAI_C = ['bagas','nasrul','amin','hamam','ridwan','andi','dadang']
siswa = 'handi'
if siswa in PAI_C:
    print(siswa,'adalah murid PAI_C')
if not siswa in PAI_C:
    print(siswa,'bukanlah murid PAI_C')
if 'n' in siswa:
    print("n ada di",siswa)
karakter = 'r'
if karakter in siswa:
    print(karakter,'ada di',siswa)
else:
    print(karakter,'tidak ada di',siswa)
    





