# operasi artimatika

a = 10
b = 3 

# Operasi Pertambahan + 
hasil = a + b 
print(a,"+", b, '=',hasil)

# Operasi Pengurangan -
hasil = a - b 
print(a,"-", b, '=',hasil)

# Operasi Perkalian *
hasil = a * b 
print(a,"*", b, '=',hasil)

# Operasi Pembagian /
hasil = a / b 
print(a,"/", b, '=',hasil) # saat pembagian otomatis langsung menjadi float

# Operasi Eksponen (pangkat) **
hasil = a ** b 
print(a,"**", b, '=',hasil)

# Operasi Modulus (sisa pembagian) %
hasil = a % b 
print(a,"%", b, '=',hasil)

# Operasi Floor Division //
hasil = a // b 
print(a,"//", b, '=',hasil) # hasil dari pembulatan pembagian ke bawah

# Prioritas Operasi, Operational Precedence
'''
    URUTAN YANG MENGAMBIL LANGKAH DULUAN ADALAH
    1. ()
    2. Eksponen
    3. Perkalian dan teman temannya * / ** % //
    4. Pertambahan dan pengurangan
'''
x = 3
y = 2
z = 4 

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, hasil)

# Kurung akan mengambil langkah duluan atau pertama
hasil = z * y + x
print( '(', z,'*',y,') +',x, '=', hasil)
