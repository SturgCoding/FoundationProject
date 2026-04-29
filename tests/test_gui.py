"""
GUI module tests for the Foundation Project.
Verifies that the GUI module can be imported and contains the required entry point.
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestGUI(unittest.TestCase):
    """
    Test suite for the GUI module.
    Primarily focuses on importability and existence of key functions.
    """
    def test_gui_imports(self):
        """Verify that the gui module is present and has the run_gui function."""
        try:
            import gui
            self.assertTrue(hasattr(gui, 'run_gui'))
        except Exception as e:
            self.fail(f"Could not import gui: {e}")

if __name__ == '__main__':
    unittest.main()
