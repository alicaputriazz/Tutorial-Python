# Operasi yang dapat dilakukan dengan penyingkatan  
# Operasi ditambah dengan assignment

# Contoh dalam Aritmatika biasa
a = 5 # ini adalah Assignment
print('nilai a=',a)

# Ini adalah penambahan dan pengurangan
a += 1 # artinya adalah a = a + 1 
print('nilai a += 1     -nilai a menjadi',a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2     -nilai a menjadi',a)

# perkalian 
a *= 2 # artinya adalah a = a * 2
print('nilai a *= 2     -nilai a menjadi',a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2     -niai a menjadi',a) # Hasilnya langsung akan menjadi Float

# ini adalah modulus dan floor division
b = 10
print('\nnilai b =', b)

b %= 3
print('nilai b %= 3  -nilai b menjadi',b)

b = 10
print('\nnilai b =', b)

b //= 3
print('nilai b //= 3  -nilai b menjadi',b)

# ini adalah pangkat / eksponen 
a = 5 
print('\nnilai a', a)
a **= 3
print('nilai a //= 3  -nilai a menjadi',a)


# Contoh dalam Operasi Bitwise
#OR
c = True
print('\nnilai c', c)
c |= False
print("nilai c |= False, nilai c menjadi", c)
c = False
print('nilai c', c)
c |= False
print("nilai c |= False, nilai c menjadi", c)

# AND
c = True
print('\nnilai c', c)
c &= False
print("nilai c &= False, nilai c menjadi", c)
c = True
print('nilai c', c)
c &= True
print("nilai c &= True, nilai c menjadi", c)

#XOR
c = True
print('\nnilai c', c)
c ^= False
print("nilai c ^= False, nilai c menjadi", c)
c = True
print('nilai c', c)
c ^= True
print("nilai c ^= True, nilai c menjadi", c)

# geser - geser
d = 0b0100
print("\nnilai d =", format(d,'04b'))
d >>= 2 
print('nilai d >>= 2     nilai d menjadi',format(d,"04b"))
d <<= 2 
print('nilai d <<= 2     nilai d menjadi',format(d,"04b"))