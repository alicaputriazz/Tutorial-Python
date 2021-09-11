# Episode input user

data = input("Masukan nama kamu = ") # trigger input hanya kenal dengan tipe data string sebelum di casting
print("data =", data, "type =", type(data))

# Jika kita ingin mengambil int, maka
angka = float (input("Masukan kata sandi = ")) # int dan float sama 
angka = int (input("Masukan kata sandi = "))
print("data =", angka, "type =", type(angka))

# Bagaimana dengan Boolean
biner = bool(input("masukan nilai boolean = ")) # Maka nilainya dalah TRUE
print("data =", biner, "type =", type(biner))

# Bagaimana caranya mengubah Boolean menjadi nilai FALSE
biner = bool(int(input("masukan nilai boolean = "))) # WAJIB di CASTING ke Integer terlebih dahulu agar nilainya FALSE
print("data =", biner, "type =", type(biner))   
 
