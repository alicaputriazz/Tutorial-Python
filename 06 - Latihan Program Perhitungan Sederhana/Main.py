# latihan konversi satuan temperatur 

# Program konversi celcius ke satuan lain

'''print("PROGRAM KONVERSI CELCIUS TEMPERATUR")
celcius = float(input('Masukan suhu kedalam celcius : '))
print('suhu adalah', celcius, "celcius" )

# Reamur
reamur = ((4/5) * celcius)
print('suhu dalam reamur adalah  ', reamur, 'reamur' )

# Fahrenheit
fahrenheit = ((9/5) * celcius)
print('suhu dalam fahrenheit adalah  ', fahrenheit, 'fahrenheit' )

# Kelvin
kelvin = celcius + 273
print('suhu dalam kelvin adalah  ', kelvin, 'kelvin' )'''

print('Fahrenheit mencari Kelvin')
fahrenheit = float(input('Masukan suhu kedalam fahrenheit : '))
print('suhunya adalah', fahrenheit, 'fahrenheit')

# Celcius
celcius = 5/9 * (fahrenheit - 32)
print('suhu fahrenrenheit dalam celcius adalah', celcius, 'celcius')

#kelvin
kelvin =  celcius + 273
print('suhu celcius dalam kelvin adalah', kelvin, 'kelvin')

print('kelvin mencari fahrenheit')
fahrenheit = 9/5 * celcius + 32
print('suhu kelvin dalam fahrenheit adalah', fahrenheit, 'fahrenheit')
 