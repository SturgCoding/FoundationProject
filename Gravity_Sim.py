"""
    File: Gravity_Sim.py
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
# Class definition - Pages; questions; vars/locations
# ==========================================

class Bean_Can:
    def __init__(self, root):
        self.root = root
        self.root.title("Bean Screen")
        self.root.geometry("800x600")
        self.root.resizable(True, True) # Width, Height resizable?

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
        self.Quit.place(x=50, y=50, width=120, height=36)

        # frame_1
        self.frame_main = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_main.place(x=50, y=100, width=710, height=460)

        # Clear_Ans
        self.Clear_Ans = tk.Button(
            self.root,
            text="Clear",
            bg="#f73b3b",
            font=("Courier New", 12),
            command=self.on_Clear_Ans_click
        )
        self.Clear_Ans.place(x=370, y=450, width=120, height=36)

        # Submit
        self.Submit = tk.Button(
            self.root,
            text="Submit",
            bg="#8ddb62",
            font=("Courier New", 12),
            command=self.on_Submit_click
        )
        self.Submit.place(x=620, y=450, width=120, height=36)

#---------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

    def on_Quit_click(self):
        """
        Handle on_Quit_click event
        Procedure: Exit/Close program
        """
        self.root.destroy()

    def on_Clear_Ans_click(self):
        """
        Handle on_Clear_Ans_click event
        TODO: Implement code here
        """
        pass

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

if __name__ == "__main__":
    print(f"TKinter Version {tk.TkVersion}")
    root = tk.Tk()
    app = Bean_Can(root)
    root.mainloop()
