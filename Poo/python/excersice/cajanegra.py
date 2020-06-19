import unittest

def suma(num1, num2):
    return abs(num1)+num2

class cajanegraTest (unittest.TestCase):
    def test_suma(self):
        num1 = 10
        num2 = 4
        result = suma(num1, num2)
        self.assertEqual(result, 14)
    
    def test_negativo(self):
        num1 = -2
        num2 = -8
        result = suma(num1,num2)
        self.assertEqual(result, -10)


if __name__ == "__main__":
    unittest.main()
    
