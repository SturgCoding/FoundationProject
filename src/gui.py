"""
    File: gui.py (old name: Gravity_Sim.py)
    Project: Foundation-CompApps
    Purpose: To provide GUI for the project and the code interface in order to edit, modify and update the GUI
            for the purposes of the project.
"""


import tkinter as tk
import customtkinter as ctk
import multiprocessing as mp

class Bean_Can:
    def __init__(self, root, queue = None):
        self.queue = queue
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
        self.Quit = ctk.CTkButton(      #custom designed button 
            master = self.root,
            text="Quit",
            command=self.on_Quit_click,
            font=("Courier New", 12, "bold"),
            border_width = 2,       #new gui designer library
            border_color= "#000000",
            fg_color= "#f73b3b",
            hover_color= "light blue",
            text_color= "#000000",
            corner_radius = 10
        )
        self.Quit.place(x=width-370, y=height-380)#, width=120, height=36
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
        self.mass_display = tk.StringVar(value="5.00")
        self.mass = tk.DoubleVar(value=5)
            # Scale
        self.Mass = ctk.CTkSlider( # Use Mass.get() to obtain value
            self.root,
            from_=0.01,
            to=100,
            orientation = tk.VERTICAL,
            number_of_steps = 10**15, #to produce less error, this value needs to be big
            variable = self.mass,
            command = lambda val1: self.mass_display.set(f"{float(val1):.2f}"), #making it to 2 d.p. with sent value being to ? d.p.
            fg_color= "light green",
            border_width = 2,
            border_color = "#000000",
            progress_color = "light green",
            button_color = "green",
            button_hover_color = "#FFFFFF",
            width = 15, 
            height = 290  #the value's resolution depends on height...
        )
        self.Mass.place(x=width-230, y=height-340)
            # Text
        self.M_Text = tk.Label(
            self.root,
            text="Mass",
        )
        self.M_Text.place(x=width-350, y=height-340, width=80, height=20)
            # Entry
        self.textvariable = tk.StringVar(value = self.mass)
        self.M_Entry = tk.Entry(
            self.root,
            font=("Courier New", 12),
            textvariable = self.mass_display
        )
        def mass_displayed(event):
            val2 = float(self.mass_display.get())
            min_val = self.Mass.cget("from_")
            max_val = self.Mass.cget("to")
            if val2 > max_val:
                val2 = max_val
            elif val2 < min_val:
                val2 = min_val
            self.mass.set(val2)
            self.mass_display.set(f"{float(val2):.2f}")
            
        self.M_Entry.bind("<Return>", mass_displayed) #displaying value, not cut off after 2 d.p.
        self.M_Entry.place(x=width-350, y=height-320, width=80, height=20)
        #----------------------------------------------------------------
        # Gravity
        self.gravity = tk.DoubleVar(value=9.81) # Set value to Earth's G as default
        self.gravity_display = tk.StringVar(value = "9.81")
            #Scale
        self.Gravity = ctk.CTkSlider( # Use Gravity.get() to obtain value
            self.root,
            from_=-9.81,
            to=50,
            orientation=tk.VERTICAL,
            number_of_steps = 10**15, #to produce less error, this value needs to be big
            variable = self.gravity,
            command = lambda val3: self.gravity_display.set(f"{float(val3):.2f}"), #making it to 2 d.p. with sent value being to ? d.p.
            fg_color= "light green",
            border_width = 2,
            border_color = "#000000",
            progress_color = "light green",
            button_color = "green",
            button_hover_color = "#FFFFFF",
            width = 15, 
            height = 290  #the value's resolution depends on height...
        )
        self.Gravity.place(x=width-200, y=height-340) # width=90, height=300
            # Text
        self.G_Text = tk.Label(
            self.root,
            text="Gravity",
        )
        self.G_Text.place(x=width-130, y=height-340, width=80, height=20)
            # Entry
        self.G_Entry = tk.Entry(
            self.root,
            textvariable=self.gravity_display,
            font=("Courier New", 12),
        )
        def gravity_displayed(event):
            val4 = float(self.gravity_display.get())
            min_val = self.Gravity.cget("from_")
            max_val = self.Gravity.cget("to")
            if val4 > max_val:
                val4 = max_val
            elif val4 < min_val:
                val4 = min_val
            self.gravity.set(val4)
            self.gravity_display.set(f"{float(val4):.2f}")
        self.G_Entry.bind("<Return>", gravity_displayed) #displaying value, not cut off after 2 d.p.
        self.G_Entry.place(x=width-130, y=height-320, width=80, height=20)

#---------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

        # THESE ARE NEEDED TO RESET AND OBTAIN VALUES
            # CLASSES CAN MAKE OBTAINING VALUES HARD, ESPECIALLY WITH TKINTER, SO GETTERS AND SETTERS SIMPLIFY THIS
    def set_Gravity_value(self, value):
        self.Gravity.set(value)
        self.gravity_display.set(value)
    def set_Mass_value(self, value):
        self.Mass.set(value)
        self.mass_display.set(value)

    def get_Gravity_value(self):
        return round(self.Gravity.get(), 2) # Round obtained values to 2dp
    def get_Mass_value(self):
        return round(self.Mass.get(), 2)

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
        print(f"Gravity: {self.get_Gravity_value()}")
        print(f"Mass: {self.get_Mass_value()}")
        if self.queue:
            self.queue.put({
                'gravity': self.get_Gravity_value(),
                'mass': self.get_Mass_value()
            })
#-----------------------------------------------------------------
# ==========================================
# Code Base - Set response when this file is run
# ==========================================

def run_gui(queue=None):
    # queue is passed in from main.py so tkinter can send values to the simulation
    root = tk.Tk()
    app = Bean_Can(root, queue=queue)
    root.mainloop()

if __name__ == "__main__":
    run_gui()  # run standalone with no queue (for testing gui.py on its own)

