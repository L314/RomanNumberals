"""
what are the roman numerals?
I, V,  X,  L,   C,   D,    M
1, 5, 10, 50, 100, 500, 1000
Rules of RN: ordered from biggest to smallest with only exception when you make a four or nine of some sort where you do
a letter of exactly one lower than the next one.
"""
import unittest


def int_to_rn(num):
    if not isinstance(num, int):
        raise TypeError
    r_string = ""
    m = num // 1000
    num -= m * 1000
    r_string += "M" * m
    cm = num // 900
    num -= cm * 900
    r_string += "CM" * cm
    d = num // 500
    num -= d * 500
    r_string += "D" * d
    cd = num // 400
    num -= cd * 400
    r_string += "CD" * cd
    c = num // 100
    num -= c * 100
    r_string += "C" * c
    xc = num // 90
    num -= xc * 90
    r_string += "XC" * xc
    l = num // 50
    num -= l * 50
    r_string += "L" * l
    xl = num // 40
    num -= xl * 40
    r_string += "XL" * xl
    x = num // 10
    num -= x * 10
    r_string += "X" * x
    ix = num // 9
    num -= ix * 9
    r_string += "IX" * ix
    v = num // 5
    num -= v * 5
    r_string += "V" * v
    iv = num // 4
    num -= iv * 4
    r_string += "IV" * iv
    i = num
    r_string += "I" * i
    return r_string


def rn_to_int(r_string):
    val = 0
    i = 0
    while i < (len(r_string)):
        if r_string[i] == "M":
            val += 1000
            i += 1
        else:
            if r_string[i] == "C" and i+1 < len(r_string):
                if r_string[i+1] == "M":
                    val += 900
                    i += 2
            break
    while i < (len(r_string)):
        if r_string[i] == "D":
            val += 500
            i += 1
        else:
            if r_string[i] == "C" and i+1 < len(r_string):
                if r_string[i+1] == "D":
                    val += 400
                    i += 2
            break
    while i < (len(r_string)):
        if r_string[i] == "C":
            val += 100
            i += 1
        else:
            if r_string[i] == "X" and i+1 < len(r_string):
                if r_string[i+1] == "C":
                    val += 90
                    i += 2
            break
    while i < (len(r_string)):
        if r_string[i] == "L":
            val += 50
            i += 1
        else:
            if r_string[i] == "X" and i+1 < len(r_string):
                if r_string[i+1] == "L":
                    val += 40
                    i += 2
            break
    while i < (len(r_string)):
        if r_string[i] == "X":
            val += 10
            i += 1
        else:
            if r_string[i] == "I" and i+1 < len(r_string):
                if r_string[i+1] == "X":
                    val += 9
                    i += 2
            break
    while i < (len(r_string)):
        if r_string[i] == "V":
            val += 5
            i += 1
        else:
            if r_string[i] == "I" and i+1 < len(r_string):
                if r_string[i+1] == "V":
                    val += 4
                    i += 2
            break
    while i < (len(r_string)):
        if r_string[i] == "I":
            val += 1
            i += 1
        else:
            raise ValueError("Parsing Failed")

    return val

class TestNumeralMethods(unittest.TestCase):
    """with self.assertRaises(TypeError):"""

    def test_rn_one(self):
        self.assertEqual(rn_to_int("I"), 1)

    def test_rn_five(self):
        self.assertEqual(rn_to_int("V"), 5)

    def test_rn_ten(self):
        self.assertEqual(rn_to_int("X"), 10)

    def test_rn_fifty(self):
        self.assertEqual(rn_to_int("L"), 50)

    def test_rn_one_hundred(self):
        self.assertEqual(rn_to_int("C"), 100)

    def test_rn_five_hundred(self):
        self.assertEqual(rn_to_int("D"), 500)

    def test_rn_one_thousand(self):
        self.assertEqual(rn_to_int("M"), 1000)

    def test_one(self):
        self.assertEqual(int_to_rn(1), "I")

    def test_five(self):
        self.assertEqual(int_to_rn(5), "V")

    def test_ten(self):
        self.assertEqual(int_to_rn(10), "X")

    def test_fifty(self):
        self.assertEqual(int_to_rn(50), "L")

    def test_one_hundred(self):
        self.assertEqual(int_to_rn(100), "C")

    def test_five_hundred(self):
        self.assertEqual(int_to_rn(500), "D")

    def test_one_thousand(self):
        self.assertEqual(int_to_rn(1000), "M")

    def test_six(self):
        self.assertEqual(int_to_rn(6), "VI")

    def test_four(self):
        self.assertEqual(int_to_rn(4), "IV")

    def test_1758(self):
        self.assertEqual(int_to_rn(1758), "MDCCLVIII")

    def test_rn_1758(self):
        self.assertEqual(rn_to_int("MDCCLVIII"), 1758)

    def test_1999(self):
        self.assertEqual(int_to_rn(1999), "MCMXCIX")

    def test_rn_1999(self):
        self.assertEqual(rn_to_int("MCMXCIX"), 1999)

    def test_all(self):
        for i in range(1, 9000):
            self.assertEqual(rn_to_int(int_to_rn(i)), i)

    def test_q_fail(self):
        with self.assertRaises(ValueError):
            rn_to_int("q")

    def test_lower_case_fail(self):
        with self.assertRaises(ValueError):
            rn_to_int("i")

if __name__ == '__main__':
    unittest.main()
