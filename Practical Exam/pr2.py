def tempConvert():
  cels = float(input("Enter temperature in celsius: "))
  fh = (cels * 9/5) + 32
  print('%.2f Celsius is: %0.2f Fahrenheit' %(cels, fh))

tempConvert()