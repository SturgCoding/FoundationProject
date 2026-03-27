import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestGUI(unittest.TestCase):
    def test_gui_imports(self):
        try:
            import gui
            self.assertTrue(hasattr(gui, 'run_gui'))
        except Exception as e:
            self.fail(f"Could not import gui: {e}")

if __name__ == '__main__':
    unittest.main()
