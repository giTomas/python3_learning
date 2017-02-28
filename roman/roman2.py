#!/usr/bin/python3

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(n):
    '''convert integer to roman numeral'''
    if n > 3999:
        raise OutOfRangeError('number out of range (must be less than 4000)')

    result = ''
    for numeral, integer in roman_numeral_map:
        #prejde vsetky tuple
        while n >= integer:
            # spusti sa iba ak je integer rovne, alebo vacsie ako int
            result += numeral
            n -= integer
            # print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
    return result
    
#trieda na odchytavanie tried
class OutOfRangeError(ValueError):
    pass
