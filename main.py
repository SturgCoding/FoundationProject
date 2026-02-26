
"""
    File: main.py
    Project: Foundation-CompApps
    Purpose: Run everything from this file, including the GUI and the physics engine.(python main.py)
"""

import multiprocessing as mp
import gui
import physics

if __name__ == "__main__":
    # Create processes for GUI and physics engine
    gui_process = mp.Process(target=gui.run_gui)
    physics_process = mp.Process(target=physics.run_physics)

    # Start the processes
    gui_process.start()
    physics_process.start()

    # Wait for both processes to finish
    gui_process.join()
    physics_process.join()