"""
Tests for maximum velocity tracking in the physics engine.
Specifically verifies that PhysicsBody correctly stores and updates vxmax and vymax.
"""
import unittest
import sys
import os

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from physics import PhysicsBody

class TestMaxVelocity(unittest.TestCase):
    """
    Test suite for maximum velocity tracking.
    Ensures that the absolute maximum velocities are recorded throughout a simulation run.
    """
    def test_max_velocity_tracking(self):
        """
        Verify that vxmax and vymax capture the highest absolute velocity values
        reached during updates, and do not decrease when velocity magnitude drops.
        """
        body = PhysicsBody(0, 0)
        # Initially 0
        self.assertEqual(body.vxmax, 0.0)
        self.assertEqual(body.vymax, 0.0)
        
        # Release with some velocity
        body.release(vx_ms=10.0, vy_ms=-5.0)
        
        # Update should capture these as max
        body.update(0.1)
        self.assertEqual(body.vxmax, 10.0)
        self.assertEqual(body.vymax, abs(body.vy)) # vy increases due to gravity
        
        last_vymax = body.vymax
        
        # Another update, vy should increase (gravity is positive 9.81)
        # However, body.update(0.1) calculates from launch point:
        # v = u + a * t
        # First update t=0.1: vy = -5 + 9.81 * 0.1 = -4.019. abs(vy) = 4.019
        # Second update t=0.2 (since 0.1+0.1=0.2): vy = -5 + 9.81 * 0.2 = -3.038. abs(vy) = 3.038
        # Wait, the vymax should be 5.0 initially? 
        # Actually vymax is updated AFTER self.vy is calculated in update().
        
        body.update(0.1)
        # t is now 0.3. vy = -5 + 9.81 * 0.3 = -2.057. abs(vy) = 2.057
        # vymax should still be 4.019 (from first update)
        self.assertEqual(body.vymax, 4.019) 
        
        # Check if vxmax stays same if vx doesn't change
        self.assertEqual(body.vxmax, 10.0)
        
        # Force a higher vx to see if vxmax updates
        # Since update() recalculates vx from ux and ax, setting body.vx manually won't work 
        # unless we change ux or ax.
        body.ux = 15.0
        body.update(0.1)
        self.assertEqual(body.vxmax, 15.0)
        
        # Force a negative vx with higher magnitude
        body.ux = -20.0
        body.update(0.1)
        self.assertEqual(body.vxmax, 20.0)

if __name__ == '__main__':
    unittest.main()
