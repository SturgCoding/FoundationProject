"""
Simulation tests for the Foundation Project.
This module verifies the behavior of game objects like BeanCan within the simulation environment.
Note: Requires a functional Pygame display environment.
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from simulation import BeanCan

class TestSimulation(unittest.TestCase):
    """
    Test suite for simulation logic and entities.
    Checks initialization and state management of simulated objects.
    """
    def setUp(self):
        import pygame
        pygame.init() # Needed for pygame.image.load inside BeanCan
        pygame.display.set_mode((1, 1))

    def tearDown(self):
        import pygame
        pygame.quit()

    def test_bean_can_init(self):
        """Test the initialization of the BeanCan object including its rect and physics properties."""
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