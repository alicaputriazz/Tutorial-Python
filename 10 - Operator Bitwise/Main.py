# operator Bitwise, operasi biner, binary.

# apa itu bitwise? Operasi pertambahan atau penggabungan antara biner yang satu dengan biner yang lain.

a = 9
b = 5

 # Bitwise OR (|) [ UNTUK BINER/ BITWISE MENGGUNAKAN SIMBOL PALANG, SEMENTARA BOOLEAN MENGGUNAKAN "OR" ]
c = a | b 
print("\n===========OR=========")
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('------------------------------------(|)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Bitwise AND (&)
c = a & b 
print("\n===========AND=========")
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('------------------------------------(&)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b 
print("\n===========XOR=========")
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('------------------------------------(^)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Bitwise NOT # hati-hati saat memakainya karena bisa jadi minus saat di mirror
c = ~a 
print("\n===========NOT=========")
print('nilai :',a,' , binary :',format(a,'08b'))
print('------------------------------------(~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print('------------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('Nilai :',e^d,', binary :', format(e^d,'08b')) # Akan menjadi flip

# Shifting 
# Shifting Right (>>)
c = a >> 3
print("\n===========Shift Right=========")
print('nilai :',a,' , binary :',format(a,'08b'))
print('------------------------------------(>>)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Shifting Left (>>)
c = a << 3
print("\n===========Shift left=========")
print('nilai :',a,' , binary :',format(a,'08b'))
print('------------------------------------(<<)')
print('nilai :',c,' , binary :',format(c,'08b'))
