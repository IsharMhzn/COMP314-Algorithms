from search_algos import linear_search, binary_search
import unittest

class TestSearch(unittest.TestCase):
    '''Test cases for search algorithms'''

    #Test suite
    def test_linear_search(self): #Test case
        '''Test Assertions for linear search'''
        values = [2, 6, 7, 1, 3, 5, 44, 25]
        self.assertEqual(linear_search(values, 7), 2)
        self.assertEqual(linear_search(values, 44), 6)
        self.assertEqual(linear_search(values, 2), 0)
        self.assertEqual(linear_search(values, 12), -1)
    
    def test_binary_search(self): #Test case
        '''Test Assertions for binary search'''
        values = [3, 9, 45, 88, 124, 659, 999]
        self.assertEqual(binary_search(values, 45, 0, len(values)), 2)
        self.assertEqual(binary_search(values, 88, 0, len(values)), 3)
        self.assertEqual(binary_search(values, 3, 0, len(values)), 0)
        self.assertEqual(binary_search(values, 999, 0, len(values)), 6)
        self.assertEqual(binary_search(values, 656, 0, len(values)), -1)

if __name__ == "__main__":
    unittest.main() #Test runner
