# Width and multiline 

# Data

data_nama = "Johnny Orlando"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string 
data_string = f"nama = {data_nama} , umur = {data_umur} , tinggi = {data_tinggi} , sepatu = {data_nomor_sepatu}"
print(5*"="+"DATA"+5*"=")
print(data_string)

# string multiline (dengan muenggunakan enter, newline, \n)
data_string = f"nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"DATA"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"DATA"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Johnny"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>6}
tinggi = {data_tinggi:>6}
sepatu = {data_nomor_sepatu:>6}
"""
print("\n"+5*"="+"DATA"+5*"=")
print(data_string)