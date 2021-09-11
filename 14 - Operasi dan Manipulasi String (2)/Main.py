# operator dalam bentuk methods

## merubah case dari string
# apa itu case? case itu contohnya misal uppercase dan lowercase

# merubah semuanya ke upper case

salam = "wassup bro!"
print("versi normal = " + salam)
salam = salam.upper() # triggernya adalah upper untuk kapital semua
print("versi upper = " + salam)

# merubah semua ke lower case
alay = "aKu cAkeEp AbIIeEeEEZzzzZZ"
print("versi normal = " + alay)
alay = alay.lower()
print("versi lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "hey sist!"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower)) # hasilnya akan bool, maka harus di casting str terlebih dahulu
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek semuanya huruf
# isalnum() <--- untuk mengecek huruf dan angka (biasanya di password) 
# isdecimal() <--- untuk mengecek angka saja
# isspace() <--- untuk mengecek kalo dia string kosong, seperti spasi, tab \t, newline \n
# istitle() <--- untuk mengecek semua kata dimulai dengan huruf besar

# contoh dari istitle
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title " + str(cek_judul)) 

## mengecek komponen startwith() endswith()
cek_start = "Sangjangnim oppa".startswith("Sangjangnim") # startswith sangat sensitif dengan uppercase dan lowercae 
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
# join()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

# split()
gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm')) # akan langsung split ke data pisah atau join()

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,"^")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip("^") # menghilangkan tanda ^
print("'"+tengah+"'")

