fahreinheit = float(input('Masukkan suhu dalam fahrenheit : '))
print('Suhu dalam Fahreinheit :', fahreinheit , "F")

celcius = 5 / 9 * (fahreinheit - 32)
print('Suhu dalam celcius : ' , celcius, 'C')

reamur = 4 / 9 * (fahreinheit - 32)
print('Suhu dalam reamur : ' , reamur, 'R')

kelvin = celcius + 273.15
print('Suhu dalam kelvin : ' , kelvin , 'K')