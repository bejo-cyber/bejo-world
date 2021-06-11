# fungsi dengan return value
def kuadrat(argument):
    total = argument**2
    print('kuadrat dari',argument,'adalah',total)
    return total

a = kuadrat(4)
print(a)
print(kuadrat(4))

print('1==============================')
# fungsi dengan value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total
def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'*',argumen2,'=',total)
    return total
    
a = tambah(9,4)
b = kali(2,5)
print(a)
print(b)
print('==============================')
c = kali(2,tambah(3,3))
print(c)
