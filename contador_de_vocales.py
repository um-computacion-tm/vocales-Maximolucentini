import unittest



def contar_vocales(mi_string):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    for letra in mi_string.lower():
        
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1 
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('msn')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('las')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_enciclopedia(self):
        resultado = contar_vocales('enciclopedia')
        self.assertEqual(resultado, {'e': 2, 'i': 2, 'a': 1, 'o': 1})

    def test_contar_eucalipto(self):
        resultado = contar_vocales('eucalipto')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'u': 1, 'o': 1})

    def test_contar_anagrama(self):
        resultado = contar_vocales('anagrama')
        self.assertEqual(resultado, {'a': 4})

    def test_contar_AleatOrIo(self):
        resultado = contar_vocales('AleatOrIo')
        self.assertEqual(resultado, {'a': 2, 'e': 1, 'i': 1, 'o': 2})
        
    def test_contar_dEterIOrO(self):
        resultado = contar_vocales('dEterIOrO')
        self.assertEqual(resultado, {'e': 2, 'i': 1, 'o': 2}) 
        
    def test_contar_sEcUEncIA(self):
        resultado = contar_vocales('sEcUEncIA')
        self.assertEqual(resultado, {'a': 1, 'e': 2, 'i': 1, 'u': 1})    
        
    def test_contar_abecedariO(self):
        resultado = contar_vocales('abecedariO')
        self.assertEqual(resultado, {'a': 2, 'e': 2, 'i': 1, 'o': 1})       
    


unittest.main()

