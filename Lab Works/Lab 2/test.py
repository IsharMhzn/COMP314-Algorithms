from insertion import insertion_sort
from merge import merge_sort, merge

import unittest

class SortingTestCase(unittest.TestCase):
	"""
	Test Cases for sorting algorithms
	"""

	def test_insertion_sort(self):
		''' Tests for insertion sort'''
		sample1 = [8, 4, 6, 9, 2, 1]
		sample2 = [83, -65, 87, 111, 12, -99]
		sample3 = [99, 55, 22, 11, 4, 3]
		sample4 = [1, 2, 3, 4, 5, 7, 8]
		insertion_sort(sample1)
		insertion_sort(sample2)
		insertion_sort(sample3)
		insertion_sort(sample4)
		self.assertListEqual(sample1, [1, 2, 4, 6, 8, 9])
		self.assertListEqual(sample2, [-99, -65, 12, 83, 87, 111])
		self.assertListEqual(sample3, [3, 4, 11, 22, 55, 99])
		self.assertListEqual(sample4, [1, 2, 3, 4, 5, 7, 8])

	def test_merge_sort(self):
		''' Tests for merge sort'''
		sample1 = [8, 4, 6, 9, 2, 1]
		sample2 = [83, -65, 87, 111, 12, -99]
		sample3 = [99, 55, 22, 11, 4, 3]
		sample4 = [1, 2, 3, 4, 5, 7, 8]
		merge_sort(sample1, 0, len(sample1)-1)
		merge_sort(sample2, 0, len(sample2)-1)
		merge_sort(sample3, 0, len(sample3)-1)
		merge_sort(sample4, 0, len(sample4)-1)
		self.assertListEqual(sample1, [1, 2, 4, 6, 8, 9])
		self.assertListEqual(sample2, [-99, -65, 12, 83, 87, 111])
		self.assertListEqual(sample3, [3, 4, 11, 22, 55, 99])
		self.assertListEqual(sample4, [1, 2, 3, 4, 5, 7, 8])

	def test_merge(self):
		sample1 = [5, 9, 12, 1, 3 ,4]
		sample2 = [17, 45, 99, 17, 18, 19]
		merge(sample1, 0, (len(sample1)-1)//2, len(sample1)-1)
		merge(sample2, 0, (len(sample2)-1)//2, len(sample2)-1)
		self.assertListEqual(sample1, [1, 3, 4, 5, 9, 12])
		self.assertListEqual(sample2, [17, 17, 18, 19, 45, 99])

if __name__ == "__main__":
	unittest.main()
