
# functional

# mendefinisikan fungsi
def fungsi():
    print('ini adalah fungsi')

# memanggil fungsi
fungsi()
fungsi()
fungsi()

print('1=========================')
# membuat fungsi sederhana
def suaraayam():
    print('kukuruyuuuk')
def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')
hargaayam()

print('2=========================')
# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargatotal = kg*harga
    print('harga',kg,'ayam adalah',hargatotal)

hargaayam()
hargatotalayam(5)
hargatotalayam(2)
hargatotalayam(0.5)
