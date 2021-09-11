# Operasi Komparasi untuk membandingkan nilai
# Setiap hasil dari operasi komperasi adalah BOOLEAN (true/false)
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2
# lebih besar dari >
print('========== lebih besar dari >')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil) # akan mengahasilkan false, karena nilainya sama

# kurang dari <
print('========== kurang dari <')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil) # akan mengahasilkan false, karena nilainya sama

# lebih dari sama dengan =>
print('========== lebih dari sama dengan >=')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil) # Maka akan terjadi TRUE karena mulai dari angka 2

# kurang dari sama dengan <=
print('========== kurang dari sama dengan <=')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil) # Maka akan terjadi TRUE karena mulai dari angka 2

# sama dengan (==)
print('========== sama dengan ==') # (==  artinya membandingkan) (=  artinya assignment)
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# tidak sama dengan (!=)
print('========== tidak sama dengan !=') # (==  artinya membandingkan) (=  artinya assignment)
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# is sebagai komparasi dua memory / object atau 2 variable
print('========== object identity (is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =' ,x, ',id = ', hex(id(x)))
print('nilai y =' ,y, ',id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

print('========== object identity (is not)')
x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =' ,x, ',id = ', hex(id(x)))
print('nilai y =' ,y, ',id = ', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

