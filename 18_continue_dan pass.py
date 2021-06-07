print('1=============================')
for i in range(1,11):
    if i is 6:
        print('nilai i adalah', 6)
    print('nilai saat ini adalah ',i)
else:
    print('akhir dari loop')
print('diluar loop')

print('1=============================')
for i in range(1,11):
    if i is 6:
        print('nilai i adalah', 6)
        continue # fungsinya melanjutkan ke step berikutnya
        print('cekkk') # tidak ter-print
    print('nilai saat ini adalah ',i)
else:
    print('akhir dari loop')
print('diluar loop')

print('2=============================')
for i in range(1,11):
    if i is 6:
        print('nilai i adalah', 6)
        break # fungsinya untuk mengakhiri for (terminasi)
    print('nilai saat ini adalah ',i)
else:
    print('akhir dari loop')
print('diluar loop')


print('3=============================')
for i in range(1,11):
    if i is 6:
        print('nilai i adalah', 6)
        pass
        
    print('nilai saat ini adalah ',i)
else:
    print('akhir dari loop')
print('diluar loop')