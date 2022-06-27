from fractions import Fraction
from pickletools import string4

if __name__ == "__main__":
    pi = 3.1415926536
    radius = 4.5

    area = pi * (radius ** 2)
    print('Circle area (pi . r^2) = ', area)

    #Complex Numbers
    c = 3.14 + 2.73j
    c = complex(3.14, 2.73)

    print('c.real = ', c.real)
    print('c.imag = ', c.imag)

    print('conjugado de c = ', c.conjugate())

    print('c * 2 = ', c *2)

    print('c ** 2 = ', c ** 2)

    d = 1 + 1j
    print('c - d = ', c - d)

    #Frações e Decimais
    f = Fraction(10, 6)
    print('Declaration Fraction (10,6)')
    print('f.numerator = ', f.numerator)
    print('f.denominator = ', f.denominator)


    from decimal import Decimal as D 

    print("D('3.14') = ",D('3.14'))  # pi, string, sem problemas de aproximação.
    print('D(0.1) * D(3) - D(0.3) = ', D(0.1) * D(3) - D(0.3))  # float, tem o problema de aproximação.    
    print("D('0.1') * D(3) - D('0.3') = ", D('0.1') * D(3) - D('0.3'))  # string, tudo certo.
    

    #Sequenciais Imutáveis: strings, tuples e bytes
    #4 Formas de declarar uma string

    string1 = 'Forma 1 de declarar strings'

    string2 = "Forma 2 de declarar strings"
    
    string3 = '''Forma 3 de decalrar strings.
    Inclusive, permite pulo de linhas,
    dessa forma.'''
    
    string4 = """Forma 4 de decalrar strings.
    Inclusive, permite pulo de linhas,
    dessa forma."""

    print(string1)
    print(string2)
    print(string3)
    print(string4)