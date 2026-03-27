import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from simulation import BeanCan

class TestSimulation(unittest.TestCase):
    def setUp(self):
        import pygame
        pygame.init() # Needed for pygame.image.load inside BeanCan
        pygame.display.set_mode((1, 1))

    def tearDown(self):
        import pygame
        pygame.quit()

    def test_bean_can_init(self):
        try:
            can = BeanCan(100, 100, 800, 600)
            self.assertEqual(can.rect.x, 100)
            self.assertEqual(can.rect.y, 100)
            self.assertEqual(can.physics.mass, 0.4)
            self.assertFalse(can.dragging)
        except Exception as e:
            self.fail(f"Initialization failed: {e}")

if __name__ == '__main__':
    unittest.main()