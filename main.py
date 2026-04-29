"""
    File: main.py
    Project: Foundation-CompApps
    Purpose: Run everything from this file, including the GUI and the physics engine.(python main.py)
"""

import multiprocessing as mp
from src import gui
from src import physics
from src import simulation
import time

if __name__ == "__main__":
    mp.freeze_support()

    settings_queue = mp.Queue()  # pipe for tkinter → pygame (gravity, mass values)

    # Create processes for GUI and physics engine, sharing the queue
    gui_process = mp.Process(target=gui.run_gui, args=(settings_queue,))
    simulation_process = mp.Process(target=simulation.run_simulation, args=(settings_queue,))

    # Start the processes
    gui_process.start()
    simulation_process.start()

    #close both apps simultaneously
    while True:
        if not gui_process.is_alive():
            simulation_process.terminate()
            break
        elif not simulation_process.is_alive():
            gui_process.terminate()
            break
        time.sleep(0.1)
    # Wait for both processes to finish
    gui_process.join()
    simulation_process.join()