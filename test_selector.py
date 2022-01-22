"""Unit Testing for the Program"""
import unittest
import selector as sL


class ElementSelector(unittest.TestCase):
    """Tests all behaviours of the program"""

    def test_HappyFlow1(self):
        """Viable solution available"""
        self.assertEqual(sL.viable_solutions([2, 3, 5, 1, 3, -2], 9),
                         ([['[ 3 5 1 ]', '[ 5 1 3 ]'], ['[ 2 3 1 3 ]', '[ 3 5 3 -2 ]'],
                           ['[ 2 3 5 1 -2 ]', '[ 2 5 1 3 -2 ]']], 6))

    def test_HappyFlow2(self):
        """No Solution available"""
        self.assertEqual(sL.viable_solutions([2, 3, 5], 9), ([], 0))

    def test_Null(self):
        """Null value is passed"""
        self.assertEqual(sL.viable_solutions('NULL', 5), ([], 0))

    def test_NoValues(self):
        """No values are passed"""
        self.assertEqual(sL.viable_solutions([], 5), ([], 0))

    def test_Duplicates(self):
        """Duplicate values exist"""
        self.assertEqual(sL.viable_solutions([2, 5, 3, 2, 1, 3], 9),
                         ([['[ 2 5 2 ]', '[ 5 3 1 ]', '[ 5 1 3 ]'], ['[ 2 3 1 3 ]', '[ 3 2 1 3 ]']], 5))
