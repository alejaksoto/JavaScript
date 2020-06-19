import  unittest

def es_mayor_edad (edad):
    if edad>=18:
        return True
    else:
        return False

class pruebasdecristalTest(unittest.TestCase):
        def test_es_mayor (self):
            edad = 20
            result= es_mayor_edad(edad)
            self.assertEquals(result,True)

        def test_es_menor(self):
            edad = 10
            result= es_mayor_edad(edad)
            self.assertEqual(result,False)
      

if __name__ == "__main__":
    unittest.main()