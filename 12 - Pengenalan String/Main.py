data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'ini menggunakan single quote' # space atau spasi juga termasuk string loh!
print(data)

data = "ini menggunakan double qoute"
print(data)

#bisa tidak pake dua duanya? Bisa dooong! kita contoh seperti percakapan!
print('"Hi,hellow fellow British man!"')
print("'Hi,hellow fellow Spanish man!'")
print("ini adalah hari Jum'at") # harus memakai kutip dua agar kutip satu (') tetap terbaca string

# 2. Menggunakan tanda ' menjadi string 
'''print('mari shalat jum'at')'''
# maka syntax akan invalid karena tanda kutip sudah ketutup pada awal at, bagaimana caranya agar ' kebaca gunakan tanda (\)
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
#print('C:\user\Ucup')# gak bisa di kutip tiga error, jadi pake tagar
# maka syntax akan error/bingung karena backlash di anggap sebagai karakter khusus
# bagaimana caranya agar backlash di print sebagai backlash? gunakan double backlash :) !
print('C:\\user\\Ucup')
# gak bisa di kutip tiga error, jadi pake tagar
# tab
print('ucup\totong, jauhan')
print('ucup\t\t\t\t\totong, semakin jauhan')

# backspace
print('ucup \botong, ucup dan otong jadi deketan')

# newline
print('baris pertama.\nbaris kedua.') # LF -> Line Feed -> unix, macos.linus
print('baris pertama.\rbaris kedua.') # cr -> Carriage return -> commodore, acorn, lisp
print('baris pertama.\r\nbaris kedua.') # CRLF -> Line Feed Carriage Return -> dipakai oleh windows

# 3. String Literal atau Raw

# hati - hati
print('C:\new folder') # akan salah pathnya, dia akan meng-enter karena ada trigger \n

# caranya menggunakan raw string 
print(r'C:\new folder') # kalo kita menggunakan trigger 'r', maka semuanya akan di anggap string 

# multiline literal string
print('''
Nama : Johnny orlando
Kelas : Freshman baru lulus kemaren
''')

# multiline literal string dan raw
print(r'''
Nama : Johnny orlando
Kelas : Freshman baru lulus kemaren \new husband
Website : www.Johnny.com/USA
''')