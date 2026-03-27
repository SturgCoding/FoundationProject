import unittest
import sys
import os
import multiprocessing as mp

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

class TestMain(unittest.TestCase):
    def test_imports(self):
        try:
            import main
            self.assertTrue(hasattr(main, 'mp'))
        except Exception as e:
            self.fail(f"Could not import main: {e}")

if __name__ == '__main__':
    unittest.main()
