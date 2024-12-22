import konversi_celcius as modul_celcius

#  input suhu manual
celcius = 23;
kelvin = celcius + 273;

# celcius_to_kelvin(celcius); # --> ini tidak bis

modul_celcius.celcius_to_fahrenheit(celcius)


#  ini meminta input suhu celcius dari user 
suhu = str(input('mau konversi ke suhu apa?'))
if suhu == 'kelvin':
    celcius = float(input('masukkan suhu dalam celcius: '))
    kelvin = modul_celcius.celcius_to_kelvin(celcius);
    print(f'suhu {celcius} derjat celcius ke kelvin adalah {kelvin}')













