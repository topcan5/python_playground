  # The code to test
import unittest   # The test framework
import sys, os

sys.path.append('/Users/gesong/workspace/python_playground/unit_test')

from app import my_module as my_module

class TestMyModule(unittest.TestCase):
    def test_add(self):
        # print("Current Working Directory:", os.getcwd())
        self.assertEqual(my_module.add(1,3), 4)

if __name__ == '__main__':
    unittest.main()