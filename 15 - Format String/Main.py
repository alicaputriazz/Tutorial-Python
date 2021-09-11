# format string

# contoh generik 
# string
nama = 'Marlene'
format_str = f"hallo {nama}" # depannya pake f untuk format dan kurung kurawal {}
print(format_str)

# boolean
boolean = True
format_str = f'boolean = {boolean}'
print(format_str) 

# angka
angka = 2005.5
format_str = f'angka = {angka}'# tidak usah di casting seperti sebelumnya 
print(format_str)

# bilangan bulat 
angka = 15 
format_str = f'bilangan bulat = {angka:d}' # "d" artinya untuk menampilkan bahwa angka adalah bilangan bulat
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'jutaan = {angka:,}' # "," koma untuk langsung menambahkan di bilangan ribuan
print(format_str)

# bilangan desimal
angka = 2005.3486309
format_str = f'desimal = {angka:.3f}' # "." titik untuk menandakan float atau angka dibelakang titik dan "f" menandakan float
print(format_str)

# menampilkan leading zero
angka = 2008.593462
format_str = f'desimal = {angka:010.3f}' # "010" (0) akan menambahkan dua 00 didepan angka
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.12345
format_minus = f'minus = {angka_minus:+d}'
format_plus = f'plus = {angka_plus:+.2f}'

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persentase = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total barang = Rp. {harga*jumlah:,}"
print(format_string)


