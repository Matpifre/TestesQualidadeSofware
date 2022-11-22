import unittest
from scrapper import *

class TestGetInfo(unittest.TestCase):
           
    def test_preco_gol(self):
        obtido = golPreco()
        msgEr = "ERRO - Preço inserido incorreto"
        msgCorr = "SUCESSO - Print certo de todos os preços"
        self.assertEqual(obtido[0], '2392', 'SUCESSO')
        
    def test_preco_latam(self):
        obtido = latamPreco()
        msgEr = "ERRO - Preço inserido incorreto"
        msgCorr = "SUCESSO - Print certo de todos os preços"
        self.assertEqual(obtido[0], '3058', 'SUCESSO')

    def test_preco_azul(self):
        obtido = azulPreco()
        msgEr = "ERRO - Preço inserido incorreto"
        msgCorr = "SUCESSO - Print certo de todos os preços"
        self.assertEqual(obtido[0], '1905', 'SUCESSO')
 
if __name__ == '__main__':
    unittest.main()
