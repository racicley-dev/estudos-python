print('*' * 100)
print('*' * 30, ' ' * 13, 'Operadores', ' ' * 13, '*' * 30)
print('*' * 100)
a = 14
b = 3

print('a = ', a,'\n')

print('b = ', b,'\n')

print('a + b = ',a + b,'\n')  # addition

print('a - b = ',a - b,'\n')  # subtraction

print('a * b = ',a * b,'\n')  # multiplication

print('a / b = ',a / b,'\n')  # true division

print('a // b = ',a // b,'\n')  # integer division

print('a % b = ',a % b,'\n')  # modulo operation (reminder of division,'\n')

print('a ** b = ',a ** b,'\n')  # power operation

## Part 2

print('7 / 4 = ', 7 / 4,'\n')  # true division

print('7 // 4 = ',7 // 4,'\n')  # integer division, truncation returns 1

print('-7 / 4 = ',-7 / 4,'\n')  # true division again, result is opposite of previous

print('-7 // 4 = ',-7 // 4,'\n')  # integer div., result not the opposite of previous

print('*' * 100)
print('*' * 100)

## Part 3

print('int(1.75) = ',int(1.75))

print('int(-1.75) = ', int(-1.75))

print('int(\'10110\', base=2) = ', int('10110', base=2))

print('*' * 100)
print('*' * 100)

print('pow(10, 3) = ', pow(10, 3) )

print('10 ** 3 = ', 10 ** 3)

print('pow(10, -3) = ', pow(10, -3))

print('10 ** -3 = ', 10 ** -3)

print('10 % 3 = ',10 % 3)

print('10 % 4 = ', 10 % 4)

print('*' * 100)
print('*' * 100)

print('pow(123, 4) = ', pow(123, 4))
print('pow(123, 4, 100) = ', pow(123, 4, 100))
print('pow(37, -1, 43) = ',pow(37, -1, 43))
print('7 * 37 % 43 = ', 7 * 37 % 43)

print('*' * 100)
print('*' * 100)

#make some numbers more readable, use _ underscore
n = 1_000_000_000

#Hexdecimal
hex_n = 0x_4_0_0

print('*' * 100)
print('*' * 100)

print('int(True) = ', int(True))
print('int(False) = ', int(False))
print('bool(1) = ', bool(1))
print('bool(-42) = ', bool(-42))
print('bool(0) = ', bool(0))
print('not True = ', not True)
print('not False = ', not False)
print('True and True = ', True and True)
print('True or True = ', False or True)

print('1 + True = ', 1 + True)
print('False + 42 = ', False + 42)
print('7 - True = ',7 - True)