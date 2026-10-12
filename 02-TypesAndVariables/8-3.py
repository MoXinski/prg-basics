###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

#input celcius
celcius = int(input('Enter temperature in degrees Celcius: '))
#convert to Kelvin
kelvin = celcius + 273.15
#convert to fahrenheit
fahrenheit = (celcius*1.8)+32
#print
print(f'The temperature in:\nCelcius: {celcius}\nKelvin: {kelvin}\nFahrenheit: {fahrenheit}')