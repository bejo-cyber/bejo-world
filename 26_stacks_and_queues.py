print('====STACKS====')
tumpukan = [1,2,3,4,5,6]
print('data sekarang',tumpukan)
print('1======================')
# memasukan data baru
tumpukan.append(7)
print('data masuk',7)
print('data sekarang',tumpukan)
tumpukan.append(8)
print('data masuk',8)
print('data sekarang',tumpukan)

print('2======================')
out = tumpukan.pop()
print('data keluar',out)
print('data sekarang',tumpukan)

print('====QUEUES====')

from collections import deque

antrian = deque([1,2,3,4,5])
print('data sekarang: ',antrian)


print('3======================')
# menambahkan data 
antrian.append(6)
print('data masuk: ',6)
print('data sekarang: ',antrian)

print('4======================')
antrian.append(7)
print('data masuk: ',7)
print('data sekarang:',antrian)

print('5======================')
# mengurangi antrian
out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang:',antrian)
print('6======================')
out = antrian.popleft()
print('data keluar: ',out)
print('data sekarang:',antrian)




