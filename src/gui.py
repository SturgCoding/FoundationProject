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
        self.root.update_idletasks()
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
            corner_radius = 10,
            width = 120,
            height = 24
        )
        self.Quit.place(x=width-390, y=height-60)#, width=120, height=36
            # Submit
        self.Submit = ctk.CTkButton(
            master = self.root,
            text="Submit",
            font=("Courier New", 12),
            command=self.on_Submit_click,
            border_width = 1.5,       #new gui designer library
            border_color= "#000000",
            fg_color= "#4ef73b",
            hover_color= "light blue",
            text_color= "#000000",
            corner_radius = 10,
            width=120,
            height=24
        )
        self.Submit.place(x=width-130, y=height-60) #width=120, height=36
            # Reset
        self.Reset = ctk.CTkButton(
            master = self.root,
            text="Reset",
            fg_color="#f73b3b",
            font=("Courier New", 12),
            command=self.on_Reset_click,
            border_width = 2,       #new gui designer library
            border_color= "#000000",
            hover_color= "light blue",
            text_color= "#000000",
            corner_radius = 10,
            width= 120,
            height = 24
        )
        self.Reset.place(x=width-260, y=height-60) #Adjacent to Quit    , width=120, height=36
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
            command = lambda val1: self.mass_display.set(f"{float(val1):.2f}"), #to not make new def function, lambda was used, as it can be used for 1 line def functions. val 1 just extracts the value of slider, and we put it in the entry for mass, making it to 2 d.p. with sent value being to ? d.p.
            fg_color= "light green",
            border_width = 2,
            border_color = "#000000",
            progress_color = "light green",
            button_color = "green",
            button_hover_color = "#FFFFFF",
            button_length=12,
            width = 12, 
            height = self.root.winfo_height() - 110 #the value's resolution depends on height...
        )
        self.Mass.place(x=width/2 -20, y=height-380)
            # Text
        self.M_Text = ctk.CTkLabel(
            self.root,
            text="Mass",
            font=("Ariel", 20),
            width=80, 
            height=20,
            fg_color= "transparent",
            corner_radius= 5,
            text_color= "#000000",
            justify = "center",
            anchor = "center"
        )
        self.M_Text.place(x=width-350, y=height-380)
            # Entry
        self.textvariable = tk.StringVar(value = self.mass)
        self.M_Entry = ctk.CTkEntry(
            self.root,
            font=("Courier New", 12),
            textvariable = self.mass_display,
            width=80, 
            height=24,
            corner_radius= 5,
            placeholder_text= "Enter your value",
            placeholder_text_color="#6C6C6C",
            fg_color="#ffffff",
            text_color="#000000",
            border_width= 2,
            border_color= "#000000",
            justify = "center"
        )
        def mass_displayed(event):
            try:
                val2 = float(self.mass_display.get())
            except ValueError:
                val2 = self.mass.get()  #tries whether it is number or not
            min_val = self.Mass.cget("from_")
            max_val = self.Mass.cget("to")
            if val2 > max_val:
                val2 = max_val
            elif val2 < min_val:
                val2 = min_val
            self.mass.set(val2)
            self.mass_display.set(f"{float(val2):.2f}")
            
        self.M_Entry.bind("<Return>", mass_displayed) #displaying value, not cut off after 2 d.p.
        self.M_Entry.place(x=width-350, y=height-340)
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
            command = lambda val3: self.gravity_display.set(f"{float(val3):.2f}"), #to not make new def function, lambda was used, as it can be used for 1 line def functions. val 3 just extracts the value of slider, and we put it in the entry for gravity, making it to 2 d.p. with sent value being to ? d.p.
            fg_color= "light green",
            border_width = 2,
            border_color = "#000000",
            progress_color = "light green",
            button_color = "green",
            button_hover_color = "#FFFFFF",
            button_length=12,
            width = 12, 
            height = self.root.winfo_height() - 110  #the value's resolution depends on height...
        )
        self.Gravity.place(x=width/2 + 20, y=height-380) # width=90, height=300
            # Text
        self.G_Text = ctk.CTkLabel(
            self.root,
            text="Gravity",
            font=("Ariel", 20),
            width=80, 
            height=20,
            fg_color= "transparent",
            corner_radius= 5,
            text_color= "#000000",
            justify = "center",
            anchor = "center"
        )
        self.G_Text.place(x=width-130, y=height-380)
            # Entry
        self.G_Entry = ctk.CTkEntry(
            self.root,
            textvariable=self.gravity_display,
            font=("Courier New", 12),
            width=80, 
            height=24,
            corner_radius= 5,
            placeholder_text= "Enter your value",
            placeholder_text_color="#6C6C6C",
            fg_color="#ffffff",
            text_color="#000000",
            border_width= 2,
            border_color= "#000000",
            justify = "center"
        )
        def gravity_displayed(event):
            try:
                val4 = float(self.gravity_display.get())
            except ValueError:
                val4 = self.gravity.get()
            min_val = self.Gravity.cget("from_")
            max_val = self.Gravity.cget("to")
            if val4 > max_val:
                val4 = max_val
            elif val4 < min_val:
                val4 = min_val
            self.gravity.set(val4)
            self.gravity_display.set(f"{float(val4):.2f}")
        self.G_Entry.bind("<Return>", gravity_displayed) #displaying value, not cut off after 2 d.p.
        self.G_Entry.place(x=width-130, y=height-340)

#---------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

        # THESE ARE NEEDED TO RESET AND OBTAIN VALUES
            # CLASSES CAN MAKE OBTAINING VALUES HARD, ESPECIALLY WITH TKINTER, SO GETTERS AND SETTERS SIMPLIFY THIS
    def set_Gravity_value(self, value):
        self.Gravity.set(value)
        self.gravity_display.set(value)
        self.gravity.set(value)
    def set_Mass_value(self, value):
        self.Mass.set(value)
        self.mass_display.set(value)
        self.mass.set(value)

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
        Bean_Can.set_Mass_value(self, 5.00)
        Bean_Can.set_Gravity_value(self,9.81)
        #Sending queue to the simulator that will be detected by it.
        self.queue.put({'reset': True})
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

