    # Operasi dan manipulasi string 

# 1. menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama +' '+ nama_tengah + "'"+nama_akhir # cara menempelkan semua string adalah dengan tanda '+'
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap) #spasi juga di hitung
print("panjang dari nama " + nama_lengkap + " = " + str(panjang)) # panjang akan masalah karena dia number jadi harus di crash ke str

# 3. operator untuk string

# mengecek apakah ada komponen character atau string di string
#contoh
d = "d"
status = d in nama_lengkap # Trigger in untuk mengecek apakah ada "d" dalam nama lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status)) # hasilnya akan false karena d yang di trigger adalah lowercase bukan uppercase
#contoh ke-2
D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status)) # Hasilnya akan true karena "D" adalah uppercase

# ini adalah negasi dari "in"
d = "d"
status = d not in nama_lengkap # Trigger not in untuk mengecek apakah "d" tidak ada dalam nama lengkap / atau negasi "in"
print(d + " tidak ada di " + nama_lengkap + " = " + str(status)) # hasilnya akan true karena "d" tidak ada dalam ucup D'fame

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing 
# indexing adalah kita mengambil data dari string, index di trigger dengan tanda "[]"
print("index ke-0 : " + nama_lengkap[0]) # index pertama akan di mulai dari 0 dan jumlahnya akan 10 sedangkan panjang di itung biasa
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1]) # akan mengambil dari depan jika minus (-)
print("index ke-(-2) : " + nama_lengkap[-2])
# gimana kalo mau mengambil rata rata, misalnya adalah ucup
print("index ke-(0,3) : " + nama_lengkap[0:3]) # ":" di index untuk mentrigger yang artinya sampai
# hasilnya akan "ucu" yang terakhir gak di ikutin, jadi harus di lebihin 1 
print("index ke-[0,3] : " + nama_lengkap[0:4]) # maka hasilnya akan "ucup"
print("index ke-[3,7] : " + nama_lengkap[3:8])
print("index ke-[0,2.4,6,8,10] : " + nama_lengkap[0:11:2]) # nilai 2 adalah inkremen / diloncatin 2

# item paling kecil
print("item paling kecil :" + min(nama_lengkap)) # spasi paling kecil
# item paling besar
print("item paling besar :" + max(nama_lengkap)) # max dan min akan di tentukan nilai ascii atau abjad

# maksudnya nilai paling kecil dan paling besar itu apa?
ascii_code = ord(" ") # ord adalah untuk mengambil unicode-nya dari one character string
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method (string dalam method, atau nempel dalam stringnya)

data = "otong surotong pararotong"
jumlah =  data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))