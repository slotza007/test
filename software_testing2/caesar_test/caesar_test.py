from software_testing2.caesar_Cipher.caesar_Cipher import caesarCipher
import unittest

class CaesarTest(unittest.TestCase):
    def test_caesar_AAAA(self):
        text = 'AAAA'
        num_k = 5
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'FFFF')
    
    def test_caesar_focus(self):
        text = 'focus'
        num_k = 25
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'enbtr')
    
    def test_caesar_gus(self):
        text = 'gus'
        num_k = 26
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'gus')

    def test_caesar_specialChar(self):
        text = '#f@&G'
        num_k = 12
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'#r@&S')
    
    def test_caesar_Chicken(self):
        text = 'Chicken'
        num_k = 100
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'Ydeygaj')
    
    def test_caesar_Subject1(self):
        text = 'I LoVe ChOcOlAtE VeRy MuCh'
        num_k = 20
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'C FiPy WbIwIfUnY PyLs GoWb')

    def test_caesar_specialFocus(self):
        text = 'F0(U$'
        num_k = 2
        result = caesarCipher(text,num_k)
        self.assertEqual(result,'H0(W$')