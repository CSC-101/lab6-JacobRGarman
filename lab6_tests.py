import data
import lab6
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)

    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)

    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)

    # Part 1
    def test_selection_sort_books_1(self):
        books = [
            data.Book(["Author A"], "Zebra Book"),
            data.Book(["Author B"], "Apple Book"),
            data.Book(["Author C"], "Monkey Book")
        ]
        expected = [
            data.Book(["Author B"], "Apple Book"),
            data.Book(["Author C"], "Monkey Book"),
            data.Book(["Author A"], "Zebra Book")
        ]
        lab6.selection_sort_books(books)
        self.assertEqual(books, expected)

    def test_selection_sort_books_2(self):
        books = []
        expected = []
        lab6.selection_sort_books(books)
        self.assertEqual(books, expected)

    # Part 2
    def test_swap_case_1(self):
        input = "Hello World!"
        expected = "hELLO wORLD!"
        self.assertEqual(lab6.swap_case(input), expected)

    def test_swap_case_2(self):
        input = "Python3.8 is FUN!"
        expected = "pYTHON3.8 IS fun!"
        self.assertEqual(lab6.swap_case(input), expected)

    # Part 3
    def test_str_translate_1(self):
        input = "abracadabra"
        old = 'a'
        new = 'x'
        expected = "xbrxcxdxbrx"
        self.assertEqual(lab6.str_translate(input, old, new), expected)

    def test_str_translate_2(self):
        input = "hello world"
        old = 'o'
        new = '0'
        expected = "hell0 w0rld"
        self.assertEqual(lab6.str_translate(input, old, new), expected)

    # Part 4
    def test_histogram_1(self):
        input = "apple orange apple banana"
        expected = {
            "apple": 2,
            "orange": 1,
            "banana": 1
        }
        self.assertEqual(lab6.histogram(input), expected)

    def test_histogram_2(self):
        input = "dog cat dog dog cat bird"
        expected = {
            "dog": 3,
            "cat": 2,
            "bird": 1
        }
        self.assertEqual(lab6.histogram(input), expected)

if __name__ == '__main__':
    unittest.main()
