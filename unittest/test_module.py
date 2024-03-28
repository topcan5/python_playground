  # The code to test
import unittest   # The test framework
import module
# import sys, os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
# sys.path.append('app/')

# import app.calculator as calculator
# from app import my_module
# import my_module

class TestMyModule(unittest.TestCase):
    def test_add(self):
        # print("Current Working Directory:", os.getcwd())
        self.assertEqual(module.add(1,3), 4)

if __name__ == '__main__':
    unittest.main()