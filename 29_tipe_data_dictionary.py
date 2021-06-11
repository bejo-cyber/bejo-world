list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
set = {1,2,3,4,5}

# dictionary

member1 = {'ID': 101,
           'nama': 'bagas',
           'pekerjaan': 'mahasiswa',
           'status member': 'gold'
           }
print('1====================')
print(member1)
print('2====================')
print(member1['ID'])
print('3====================')
print(member1['pekerjaan'])
print('4====================')
print(member1.keys())
print('5====================')
print(member1.values())
print('6====================')
print(member1.items())




print('7====================')

member2 = {'ID': 106,
           'nama': 'bejo',
           'pekerjaan': 'bos',
           'status member': 'berlian'
           }

memberList = {101:member1,106:member2}
print(memberList[101])







