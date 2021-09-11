# Casting adalah merubah tipe data ke tipe lain 
# Tipe data itu ada = int, float, str, bool

#Integer
print("===ini adalah Integer===")
data_int = 9
print("data = ", data_int, ",type = ", type(data_int))

data_float = float (data_int)
data_str   = str (data_int)
data_bool  = bool (data_int) # Akan false jika nilai int adalah 0
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

#Float
print("====ini adalah Float===")
data_float = 9.6
print("data = ", data_float, ",type = ", type(data_float))

data_int = int (data_float) # Akan dibulatkan ke bawah
data_str   = str (data_float)
data_bool  = bool (data_float) # Akan false jika nilai float adalah 0
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

#Boolean
print("====ini adalah Boolean===")
data_bool = True
print("data = ", data_bool, ",type = ", type(data_bool))

data_int = int (data_bool) # Akan dibulatkan ke bawah
data_str   = str (data_bool)
data_float  = float (data_bool) # Akan false jika nilai float adalah 0
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_float, "type =", type(data_float))

#String
print("====ini adalah String===")
data_str = "0" 
print("data = ", data_str, ",type = ", type(data_str))

data_int = int (data_str) # String harus angka
data_float  = float (data_str) # String harus angka
data_bool   = bool (data_str) # False jika string bernilai kosong
print("data =", data_int, "type =", type(data_int))
print("data =", data_float, "type =", type(data_float))
print("data =", data_bool, "type =", type(data_bool))
