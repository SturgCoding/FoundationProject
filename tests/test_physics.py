"""
Tests for the physics engine of the Foundation Project.
This module verifies the behavior of PhysicsBody, including motion, 
gravity, and collision (bouncing) logic.
"""
import unittest
import sys
import os

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from physics import PhysicsBody, PIXELS_PER_METER, GRAVITY

class TestPhysicsBody(unittest.TestCase):
    """
    Test suite for the PhysicsBody class.
    Verifies initialization, movement, flight status, and bounce mechanics.
    """
    def setUp(self):
        self.body = PhysicsBody(100, 200, mass=2.5)

    def test_initialization(self):
        """Test that a PhysicsBody starts with correct positions, mass, and default gravity."""
        self.assertEqual(self.body.x, 100)
        self.assertEqual(self.body.y, 200)
        self.assertEqual(self.body.mass, 2.5)
        self.assertEqual(self.body.ay, GRAVITY)
        self.assertFalse(self.body.in_flight)
        self.assertFalse(self.body.grounded)

    def test_release(self):
        """Test the release method to ensure flight starts with the given initial velocities."""
        self.body.release(vx_ms=5.0, vy_ms=-2.0)
        self.assertTrue(self.body.in_flight)
        self.assertFalse(self.body.grounded)
        self.assertEqual(self.body.ux, 5.0)
        self.assertEqual(self.body.uy, -2.0)
        self.assertEqual(self.body._launch_x, 100)
        self.assertEqual(self.body._launch_y, 200)

    def test_update_in_flight(self):
        """
        Test the physics update loop.
        Verifies that velocity and position change correctly under gravity over time.
        """
        self.body.release(vx_ms=0.0, vy_ms=0.0)
        dt = 1.0 # 1 second
        self.body.update(dt)
        # v = u + at -> vy = 0 + 9.81 * 1 = 9.81
        self.assertAlmostEqual(self.body.vy, GRAVITY)
        # s = ut + 0.5at^2 -> sy = 0 + 0.5 * 9.81 * 1 = 4.905
        # y = launch_y + sy * PIXELS_PER_METER
        self.assertAlmostEqual(self.body.sy, 0.5 * GRAVITY)
        self.assertAlmostEqual(self.body.y, 200 + 0.5 * GRAVITY * PIXELS_PER_METER)

    def test_bounce(self):
        """Test the bouncing mechanic ensuring energy loss (restitution) and direction flip."""
        self.body.release(vx_ms=2.0, vy_ms=10.0)
        self.body.bounce(ground_y_px=500, restitution=0.5)
        self.assertEqual(self.body.y, 500)
        self.assertAlmostEqual(self.body.vy, -5.0) # -10 * 0.5
        self.assertTrue(self.body.in_flight)

    def test_bounce_settle(self):
        """Test that the body comes to rest if a bounce has very low velocity."""
        self.body.release(vx_ms=0.1, vy_ms=0.4)
        self.body.bounce(ground_y_px=500, restitution=0.5)
        # new_vy = -0.4 * 0.5 = -0.2 (abs < 0.3)
        self.assertFalse(self.body.in_flight)
        self.assertTrue(self.body.grounded)
        self.assertEqual(self.body.vx, 0.0)
        self.assertEqual(self.body.vy, 0.0)

if __name__ == '__main__':
    unittest.main()
