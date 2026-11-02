import unittest

from _01_xor_swap import xor_swap
from _02_single_number import single_number
from _03_remove_duplicates_hash_set import remove_duplicates
from _04_binary_search_descending import binary_search_descending
from _05_two_sum_hash_map import two_sum
from _06_valid_parentheses_stack import is_valid_parentheses
from _07_fibonacci_tabulation import fibonacci
from _08_activity_selection import activity_selection


class TestDSAPrograms(unittest.TestCase):
    def test_xor_swap(self):
        self.assertEqual(xor_swap(10, 20), (20, 10))
        self.assertEqual(xor_swap(5, 5), (5, 5))

    def test_single_number(self):
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)
        self.assertEqual(single_number([-3, 8, 8]), -3)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([4, 2, 4, 1, 2, 3, 1]), [4, 2, 1, 3])
        self.assertEqual(remove_duplicates([]), [])

    def test_descending_binary_search(self):
        values = [90, 75, 60, 45, 30, 15]
        self.assertEqual(binary_search_descending(values, 60), 2)
        self.assertEqual(binary_search_descending(values, 50), -1)
        self.assertEqual(binary_search_descending([], 5), -1)

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
        self.assertEqual(two_sum([1, 2], 10), [])

    def test_valid_parentheses(self):
        self.assertTrue(is_valid_parentheses("([]{})"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertFalse(is_valid_parentheses("((("))
        self.assertTrue(is_valid_parentheses(""))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(7), 13)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_activity_selection(self):
        activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
        self.assertEqual(activity_selection(activities), [(1, 3), (4, 6), (6, 7), (8, 9)])
        self.assertEqual(activity_selection([]), [])


if __name__ == "__main__":
    unittest.main()
