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
        self.root.title("Bean Value Screen")

        #DO NOT CHANGE VALUES, THIS MAKES IT SMALL YET CLEAR
        global width, height
        width = 400
        height = 400

        self.root.minsize(width=width, height=height) #minium size of window is set to 400x400

        self.root.geometry(f"{width}x{height}") # Set TK Window to screen size
        self.root.resizable(True, True) # Width, Height resizable bool

        # Create widgets
        self._create_widgets()

    def _create_widgets(self):
        """Create and place all widgets"""
        # Buttons
            # Quit
        self.Quit = tk.Button(
            self.root,
            text="Quit",
            bg="#f73b3b",
            font=("Courier New", 12),
            command=self.on_Quit_click
        )
        self.Quit.place(x=width-370, y=height-380, width=120, height=36)
            # Submit
        self.Submit = tk.Button(
            self.root,
            text="Submit",
            bg="#8ddb62",
            font=("Courier New", 12),
            command=self.on_Submit_click
        )
        self.Submit.place(x=width-150, y=height-380, width=120, height=36)
            # Reset
        self.Reset = tk.Button(
            self.root,
            text="Reset",
            bg="#f73b3b",
            font=("Courier New", 12),
            command=self.on_Reset_click
        )
        self.Reset.place(x=width-260, y=height-40, width=120, height=36) #Adjacent to Quit
        #----------------------------------------------------------------
        # Mass
        self.mass = tk.IntVar(value=5)
            # Scale
        self.Mass = tk.Scale( # Use Mass.get() to obtain value
            self.root,
            from_=0.1,
            to=20,
            orient=tk.VERTICAL,
            resolution=0.01,
            variable=self.mass
        )
        self.Mass.place(x=width-275, y=height-340, width=80, height=300)
            # Text
        self.M_Text = tk.Label(
            self.root,
            text="Mass",
        )
        self.M_Text.place(x=width-350, y=height-340, width=80, height=20)
            # Entry
        self.M_Entry = tk.Entry(
            self.root,
            textvariable=self.mass,
            font=("Courier New", 12),
        )
        self.M_Entry.place(x=width-350, y=height-320, width=80, height=20)
        #----------------------------------------------------------------
        # Gravity
        self.gravity = tk.DoubleVar(value=9.81) # Set value to Earth's G as default
            #Scale
        self.Gravity = tk.Scale( # Use Gravity.get() to obtain value
            self.root,
            from_=-10,
            to=20,
            orient=tk.VERTICAL,
            resolution=0.01,
            variable=self.gravity
        )
        self.Gravity.place(x=width-215, y=height-340, width=90, height=300)
            # Text
        self.G_Text = tk.Label(
            self.root,
            text="Gravity",
        )
        self.G_Text.place(x=width-130, y=height-340, width=80, height=20)
            # Entry
        self.G_Entry = tk.Entry(
            self.root,
            textvariable=self.gravity,
            font=("Courier New", 12),
        )
        self.G_Entry.place(x=width-130, y=height-320, width=80, height=20)

#---------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

        # THESE ARE NEEDED TO RESET AND OBTAIN VALUES
    def set_Gravity_value(self, value):
        self.Gravity.set(value)
    def set_Mass_value(self, value):
        self.Mass.set(value)
    def get_Gravity_value(self):
        return self.Gravity.get()
    def get_Mass_value(self):
        return self.Mass.get()

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
        Bean_Can.set_Mass_value(self, 5)
        Bean_Can.set_Gravity_value(self,9.81)
        #Reset SIM?

    def on_Submit_click(self):
        """
        Handle on_Submit_click event
        TODO: Implement code here
        """
        print(f"Gravity: {self.get_Gravity_value()}")
        print(f"Mass: {self.get_Mass_value()}")

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
