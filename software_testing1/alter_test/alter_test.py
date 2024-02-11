from software_testing1.alternating.alternating import alternatingChar
import unittest

class AlterTest(unittest.TestCase):
    def test_alter_AAAA_num(self):
        text = 'AAAA'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '3')
    
    def test_alter_focus_num(self):
        text = 'focus'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '0')
    
    def test_alter_Peeranat_num(self):
        text = 'Peeranat'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '1')

    def test_alter_manyChar_num(self):
        text = '''AABBABABBBBBABBABABBBBABBABABABBABBABBBBAAABBBBBBBBBBBABBBBBBBABBBBBBBBBBBBABBABBBBAABBBBBAAAABBBBBB'''
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '62')
    
    def test_alter_11111_num(self):
        text = '11111'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '4')
    
    def test_alter_1234_num(self):
        text = '1234'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '0')
    
    def test_alter_special_char1_num(self):
        text = '#######'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '6')
    
    def test_alter_special_char2_num(self):
        text = '#@$()**'
        num_of_alter_char = alternatingChar(text)
        self.assertEqual(num_of_alter_char, '1')
    



    

