# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

#  ++++++++3---------10++++++++

input_user = float(input('masukan angka yang bernilai \nkurang dari 3 \natau \nlebih dari 10 \n:'))

# +++++++3-------------
# memeriksa angka yg kurang dari 3
kurang_dari = input_user < 3
print('kurang dari 3 : ',kurang_dari)

#----------10++++++++++
# memeriksa angka yg lebih dari 10
lebih_dari = input_user > 10
print('lebih dari 10 : ',lebih_dari)

# ++++++++++++++3-------------10+++++++++++++++++++
hasil = kurang_dari or lebih_dari
print("hasil dari jawaban anda adalah : ",hasil)

print('***********************')
# ------------3+++++++++10-----------
# kasus irisan

#-------3+++++++++
#memeriksa angka yg lebih dari 3
input_user = float(input('masukan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10 \n:'))
lebih_dari = input_user>3
print('lebih dari 3 : ',lebih_dari)

#+++++++++10------------
# memeriksa angka yg kurang dari 10
kurang_dari = input_user<10
print('kurang dari : ', kurang_dari)

#-----3+++++10-----
hasil = lebih_dari and kurang_dari
print('hasil dari jawaban anda adalah : ',hasil)


