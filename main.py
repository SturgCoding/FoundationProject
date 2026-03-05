#########################################
# USE auto-py-to-exe TO CREATE .exe file
# https://pypi.org/project/auto-py-to-exe/
#########################################
"""
    File: main.py
    Project: Foundation-CompApps
    Purpose: Run everything from this file, including the GUI and the physics engine.(python main.py)
"""

import multiprocessing as mp
from src import gui
from src import physics
from src import simulation

if __name__ == "__main__":
    mp.freeze_support()

    # Create processes for GUI and physics engine
    gui_process = mp.Process(target=gui.run_gui)
    simulation_process = mp.Process(target=simulation.run_simulation)

    # Start the processes
    gui_process.start()
    simulation_process.start()

    # Wait for both processes to finish
    gui_process.join()
    simulation_process.join()