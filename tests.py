import unittest
from StringParser import check_sequence_same_type, check_sequence_mixed_type

class TestStringParser(unittest.TestCase):

    def test_check_sequence_same_type(self):
        self.assertTrue(check_sequence_same_type('()()'),True)
        self.assertTrue(check_sequence_same_type('(){}'),True)
        
        self.assertFalse(check_sequence_same_type('()){}'))
        self.assertFalse(check_sequence_same_type('())({}'))
        self.assertFalse(check_sequence_same_type(')('))
        self.assertTrue(check_sequence_same_type(r'(abc)(p)'))

    def test_check_sequence_mixed_type(self):
        
        self.assertTrue(check_sequence_mixed_type('([{<>}])'))
        self.assertTrue(check_sequence_mixed_type(r'(abc(p{c}))'))
        
        self.assertFalse(check_sequence_mixed_type(r')('))
        self.assertFalse(check_sequence_mixed_type(r'(())(<>)'))
        self.assertFalse(check_sequence_mixed_type('())({}'))


if __name__ == '__main__':
    unittest.main()