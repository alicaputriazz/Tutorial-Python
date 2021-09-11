# episode latihan logika dan komparasi 

# membuat gabungan dari area rentang dari angka 
# untuk penggabungan menggunakan keyword "OR"

# +++++++++3---------10++++++++++
inputUser = int(input('masukan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10\n:'))

# ++++3--------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3", isKurangDari)

# -----------10+++
# Memeriksa angka lebih dari 10 
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++++++3---------10++++++++++
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan:', isCorrect)

# -----3++++++++10--------
# kasus Irisan 
print('\n',10*'=','\n')
inputUser = float(input('masukan angka yang bernilai\n lebih dari 3 \ndan \nkurang dari 10\n:'))

# --------3++++++++++
# lebih dari 3
isLebihDari = inputUser > 3 
print('lebih dari 3 =', isLebihDari)

# ++++++++10---------
isKurangDari = inputUser < 10 
print('kurang dari 10 =', isKurangDari)

# -----3++++++++10--------
isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukan:', isCorrect)


# Latihan
print('\n ============ \n')
print('LATIHAN')

# 1.     -----0+++++5-----8+++++11-----
inputUser = float(input("masukan angka yang bernilai \n lebih dari 0 \n kurang dari 5 \n lebih dari 8 \n kurang dari 11:\n"))

#----0+++++
# memeriksa lebih dari 0
isLebihDari0 = (inputUser > 0)
print('Lebih dari 0',isLebihDari0)

#+++++5-----
isKurangDari5 = (inputUser < 5)
print('Kurang dari 5', isKurangDari5)

#-----8+++++
isLebihDari8 = (inputUser > 8)
print('Lebih dari 8', isLebihDari8) 

#+++++11-----
iskurangDari11 = (inputUser < 11)
print('kurang dari 11', iskurangDari11)

#-----0+++++5-----8+++++11-----
isCorrect = isLebihDari0 or isKurangDari5 or isLebihDari8 or iskurangDari11
print('angka yang anda masukan', isCorrect)


# Cara Cepat versi aku :)
# 2.      +++++0-----5++++++8-----11++++
inputUser = float(input("masukan angka anda :\n"))
Nol = (inputUser < 0)
Lima = (inputUser > 5)
Delapan = (inputUser < 8)
Sebelas = (inputUser > 11)

isCorrect = Nol or Lima or Delapan or Sebelas
print('angka yang anda masukan adalah', isCorrect)



'''# Mencoba cara dari komenan video orang lain
angka = int(input("masukan angka :\n"))
x = angka > 0 and angka < 5
y = angka > 8 and angka < 11
z = x or y 
print(z)'''


