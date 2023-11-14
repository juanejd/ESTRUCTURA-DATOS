from BaseGeneral import convertirBase

numeroDecimal = 233

cadenaOctal = convertirBase(numeroDecimal, 8)
cadenaDoce = convertirBase(numeroDecimal, 12)
cadenaHexadecimal = convertirBase(numeroDecimal, 16)

print('El numero decimal {} en octal es: {}. Y en hexadecimal es: {}'.format(numeroDecimal, cadenaOctal, cadenaHexadecimal))

print('El numero decimal {} en base doce es: {}'.format(numeroDecimal, cadenaDoce))