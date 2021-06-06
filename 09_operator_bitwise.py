# operator bitwise, operasi biner, binary


a = 9
b = 5
# bitwise OR (|)
c = a|b
print("\n=========OR=========")
print('nilai :',a,' , binary : ',format(a,'08b'))
print('nilai :',b,' , binary : ',format(b,'08b'))
print('------------|-----------')
print('nilai :',c,' , binary :',format(c, '08b'))

# bitwise AND (&)
c = a&b
print("\n=========AND=========")
print('nilai :',a,' , binary : ',format(a,'08b'))
print('nilai :',b,' , binary : ',format(b,'08b'))
print('------------&-----------')
print('nilai :',c,' , binary :',format(c, '08b'))

# bitwise XOR (^)
c = a^b
print("\n=========XOR=========")
print('nilai :',a,' , binary : ',format(a,'08b'))
print('nilai :',b,' , binary : ',format(b,'08b'))
print('------------^-----------')
print('nilai :',c,' , binary :',format(c, '08b'))

# bitwise NOT (~)
c = ~a
print("\n=========XOR=========")
print('nilai :',a,' , binary : ',format(a,'08b'))

print('------------~-----------')
print('nilai :',c,' , binary :',format(c, '08b'))

# shifting

# shift right (>>)
c = a >> 2
d = a >> 1
print("\n=========>>=========")
print('nilai :',a,' , binary : ',format(a,'08b'))

print('------------>>-----------')
print('nilai :',c,' , binary :',format(c, '08b'))
print('nilai :',d,' , binary :',format(d, '08b'))

# shit left (<<)
c = a << 2
d = a << 1
print("\n=========<<=========")
print('nilai :',a,' , binary : ',format(a,'08b'))

print('------------<<-----------')
print('nilai :',c,' , binary :',format(c, '08b'))
print('nilai :',d,' , binary :',format(d, '08b'))




