# latihan 

# kalkulator sederhana
print("\n"+20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukan angka 1 = "))
operator = input("operator (+,-,x,/) ")
angka_2 = float(input("masukan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukan yang benar doong, aku pusying nih")

print("akhir dari program, terima kassiiiieehhh")


    
