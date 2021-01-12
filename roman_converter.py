'''
Input : 9
Output : IX

Input : 40
Output : XL

Input :  1904
Output : MCMIV

SYMBOL       VALUE
I             1
IV            4
V             5
IX            9
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900 
M             1000    
'''

import unittest

class TestRomanConverter(unittest.TestCase):
    def test_9_to_IX(self):
        self.assertEqual(convert(9), 'IX')
    
    def test_11(self):
        self.assertEqual(convert(11), 'XI')
    
    def test_550(self):
        self.assertEqual(convert(550), 'DL')
    
    def test_1904(self):
        self.assertEqual(convert(1904), 'MCMIV')
    
    def test_3999(self):
        self.assertEqual(convert(3999), 'MMMCMXCIX')

def convert(num):
    thousands = ''
    hundred_digit = ''
    main_unit = ''
    ten_digit = ''

    if (num > 1000):
        thousands = convert_thousand_digit(num - (num % 1000))
        num = num % 1000

    if (num > 100):
        hundred_digit = convert_hundred_digit(num - (num % 100))
        num = num % 100
  
    if (num > 10):
        ten_digit = convert_ten_digit((num - (num % 10)))
        num = num % 10

    main_unit = convert_main_unit(num)
    

    return thousands + hundred_digit + ten_digit + main_unit

def convert_main_unit(num):
    if num == 1:
        return 'I'
    elif num == 4:
        return 'IV'
    elif num == '5':
        return 'V'
    elif num == 9:
        return 'IX'
    return ''

def convert_ten_digit(num):
    if num == 10:
        return 'X'
    elif num == 40:
        return 'XL'
    elif num == 50:
        return 'L'
    elif num == 90:
        return 'XC'
    return ''

def convert_hundred_digit(num):
    if num == 100:
        return 'C'
    elif num == 400:
        return 'CD'
    elif num == 500:
        return 'D'
    elif num == 900:
        return 'CM'
    return ''

def convert_thousand_digit(num):
    thousand = ''
    for _ in range(0, int(num/1000)):
        thousand += 'M'
    return thousand

if __name__ == '__main__':
    unittest.main()