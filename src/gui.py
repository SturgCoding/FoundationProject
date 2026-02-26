"""
    File: gui.py (old name: Gravity_Sim.py)
    Project: Foundation-CompApps
    Purpose: To provide GUI for the project and the code interface in order to edit, modify and update the GUI
            for the purposes of the project.
"""

#-----------------------------------------------------------------
# ==========================================
# Required imports - tkinter plus dependencies
# ==========================================

#dependancy
import tkinter as tk

#imports area: abstracted code/ideas

#-----------------------------------------------------------------
# ==========================================
# Class definition - Page(s)
# ==========================================

class Bean_Can:

    def __init__(self, root):
        self.root = root
        self.root.title("Bean Screen")

        global width, height
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        self.root.geometry(f"{width}x{height}") # Set TK Window to screen size
        self.root.resizable(False, False) # Width, Height resizable

        # Create widgets
        self._create_widgets()

    def _create_widgets(self):
        """Create and place all widgets"""

        # Quit
        self.Quit = tk.Button(
            self.root,
            text="Quit",
            bg="#f73b3b",
            font=("Courier New", 12),
            command=self.on_Quit_click
        )
        self.Quit.place(x=50, y=40, width=120, height=36)

        # frame_1
        self.frame_main = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_main.place(x=5, y=150, width=width-10, height=height-155)

        # Reset
        self.Reset = tk.Button(
            self.root,
            text="Reset",
            bg="#f73b3b",
            font=("Courier New", 12),
            command=self.on_Reset_click
        )
        self.Reset.place(x=170, y=40, width=120, height=36) #Adjacent to Quit

        self.labelVelocity = tk.Label(
            self.root,
            font=("Courier New", 12),
            text="Velocity (m/s)",
            justify=tk.LEFT, #Keep writing to lefthand side
        )
        self.labelVelocity.place(x=300, y=50, width=200, height=25)
        self.H_Velocity = tk.Scale( # Use H_Velocity.get() to obtain value
            self.root,
            from_=0,
            to=20,
            orient=tk.HORIZONTAL,
            resolution=0.1
        )
        self.H_Velocity.set(5)
        self.H_Velocity.place(x=300, y=20, width=width-480, height=36)

        self.labelGravity = tk.Label(
            self.root,
            font=("Courier New", 12),
            text="Gravity (m/s^2)",
            justify=tk.LEFT, #Keep writing to lefthand side
        )
        self.labelGravity.place(x=300, y=105, width=200, height=25)
        self.Gravity = tk.Scale( # Use Gravity.get() to obtain value
            self.root,
            from_=-20,
            to=20,
            orient=tk.HORIZONTAL,
            resolution=0.01
        )
        self.Gravity.set(9.81) # Set value to Earth's G as default
        self.Gravity.place(x=300, y=75, width=width-480, height=36)

        # Submit
        self.Submit = tk.Button(
            self.root,
            text="Submit",
            bg="#8ddb62",
            font=("Courier New", 12),
            command=self.on_Submit_click
        )
        self.Submit.place(x=width-170, y=40, width=120, height=36)

#---------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

    def set_Gravity_value(self, value):
        self.Gravity.set(value)
    def set_H_Velocity_value(self, value):
        self.H_Velocity.set(value)

    def on_Quit_click(self):
        """
        Handle on_Quit_click event
        Procedure: Exit/Close program
        """
        self.root.destroy()

    def on_Reset_click(self):
        """
        Handle on_Reset_click event
        Procedure: Reset program (to default values/start)
        TODO: FINISH CODE HERE
        """
        #Reset To Defaults
        Bean_Can.set_H_Velocity_value(self, 5)
        Bean_Can.set_Gravity_value(self,9.81)
        #Reset SIM?

    def on_Submit_click(self):
        """
        Handle on_Submit_click event
        TODO: Implement code here
        """
        pass

#-----------------------------------------------------------------
# ==========================================
# Code Base - Set response when this file is run
# ==========================================

def run_gui():
    root = tk.Tk()
    app = Bean_Can(root)
    root.mainloop()

if __name__ == "__main__":
    print(f"TKinter Version {tk.TkVersion}")
    run_gui()
