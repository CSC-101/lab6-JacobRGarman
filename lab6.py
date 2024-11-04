import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values: list[int], start: int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex

# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
def selection_sort(values: list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1

# Sorts, in place, a list of Book objects by title in alphabetical order using selection sort.
# input: a list of Book objects
# returns: nothing is returned; the list is sorted in place
def selection_sort_books(books: list[data.Book]) -> None:
    for idx in range(len(books) - 1):
        mindex = idx
        for j in range(idx + 1, len(books)):
            if books[j].title < books[mindex].title:
                mindex = j
        # Swap the Book at idx with the Book at mindex
        books[idx], books[mindex] = books[mindex], books[idx]


# Part 2

# Swaps the case of each alphabetical character in the input string.
# input: a string
# returns: a new string with cases swapped
def swap_case(s: str) -> str:
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)


# Part 3

# Replaces all occurrences of 'old' character with 'new' character in the input string.
# input: a string, the old character to replace, and the new character to replace it with
# returns: a new string with all occurrences of 'old' replaced with 'new'
def str_translate(s: str, old: str, new: str) -> str:
    result = []
    for char in s:
        if char == old:
            result.append(new)
        else:
            result.append(char)
    return ''.join(result)


# Part 4

# Creates a dictionary mapping words to their frequency count from the input string.
# input: a string
# returns: a dictionary with words as keys and their frequency counts as values
def histogram(s: str) -> dict[str, int]:
    word_counts = {}
    words = s.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
