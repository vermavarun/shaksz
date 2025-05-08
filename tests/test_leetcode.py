# tests/test_module.py

import unittest
from shaksz import leetcode

class TestModule(unittest.TestCase):
    def test_twoSum(self):
        result = leetcode.twoSum([2,7,11,15],9)
        self.assertEqual(result, [0,1])

if __name__ == '__main__':
    unittest.main()
