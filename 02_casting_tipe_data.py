#===CASTING TIPE DATA====
#merubah dari satu tipe ke tipe yang lain
#tipe data = int, str, float, bool

#1 INTEREGEN
print('====INTEREGEN====')
data_int = '9'
print("data interegen =",data_int)
data_string = str(data_int)
data_float = float(data_int)
data_boolean = bool(data_int)
print("data = ",data_string, " type =",type(data_string))
print("data = ",data_float, " type =",type(data_float))
print("data = ",data_boolean, " type =",type(data_boolean))

#2 FLOAT
print('====FLOAT====')
data_float = 9.9
print("data float =",data_float)
data_interegen = int(data_float)#akan dibulatkan ke bawah
data_string = str(data_float)
data_boolean = bool(data_float)#akan false jika nilai int = 0
print("data = ",data_interegen, " type =",type(data_interegen))
print("data = ",data_string, " type =",type(data_string))
print("data = ",data_boolean, " type =",type(data_boolean))

#BOOLEAN
print('====BOOLEAN====')
data_bool = True
print("data bool =",data_bool)
data_interegen = int(data_bool)
data_string = str(data_bool)
data_float = float(data_bool)
print("data = ",data_interegen, " type =",type(data_interegen))
print("data = ",data_string, " type =",type(data_string))
print("data = ",data_float, " type =",type(data_float))

#STRING
print('====STRING====')
data_string = "10"
print("data_string =",data_string)
data_interegen = int(data_string)#string harus angka
data_bool = bool(data_string)#false jika string kosong
data_float = float(data_string)#string harus angka
print("data = ",data_interegen, " type =",type(data_interegen))
print("data = ",data_bool, " type =",type(data_bool))
print("data = ",data_float, " type =",type(data_float))

