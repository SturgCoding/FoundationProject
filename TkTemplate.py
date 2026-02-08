    # ==========================================
    # Required imports - tkinter plus dependencies
    # ==========================================

import tkinter as tk

#import abstracted code/ideas
    #E.g. Question handling code
import Questions

#-----------------------------------------------------------------
    # ==========================================
    # Class definition - Pages; questions; vars/locations
    # ==========================================

class Q_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("Question Screen")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Initialize variables - Create object location
        self.Q_number = tk.IntVar()
        self.Ans1 = tk.BooleanVar()
        self.Ans2 = tk.BooleanVar()
        self.Ans3 = tk.BooleanVar()
        self.Ans4 = tk.BooleanVar()

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

        # Question_Area
        self.Question_Area = tk.Message(
            self.root,
            font=("Courier New", 12),
            text = "Initialized...",
            bg="#ffffff",
            fg="#000000",
            width=690 # Message needs width of box to wrap text correctly
        )
        self.Question_Area.place(x=60, y=110, width=690, height=120)

        # workings
        self.Workings = tk.Text(
            self.root,
            font=("Courier New", 12),
            bg="#ffffff",
            fg="#000000"
        )
        self.Workings.place(x=60, y=250, width=300, height=250)
        #index: line(1index).column(0index)
        self.Workings.insert(1.0, "Write workings here")  # Placeholder text

        # A_1
        self.A_1 = tk.Checkbutton(
            self.root,
            text="A_1 Initialized",
            variable=self.Ans1,
            command=self.on_A_1_click
        )
        self.A_1.place(x=380, y=260)
        # A_2
        self.A_2 = tk.Checkbutton(
            self.root,
            text="A_2 Initialized",
            variable=self.Ans2,
            command=self.on_A_2_click
        )
        self.A_2.place(x=380, y=300)
        # A_3
        self.A_3 = tk.Checkbutton(
            self.root,
            text="A_3 Initialized",
            variable=self.Ans3,
            command=self.on_A_3_click
        )
        self.A_3.place(x=380, y=340)
        # A_4
        self.A_4 = tk.Checkbutton(
            self.root,
            text="A_4 Initialized",
            variable=self.Ans4,
            command=self.on_A_4_click
        )
        self.A_4.place(x=380, y=380)

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

#-----------------------------------------------------------------
    # ==========================================
    # Get/Set Handlers - Implement change
    # ==========================================
    def get_Ans1(self):
        return self.Ans1.get()
    def set_Ans1(self, bool):
        self.Ans1.set(bool)

    def get_Ans2(self):
        return self.Ans2.get()
    def set_Ans2(self, bool):
        self.Ans2.set(bool)

    def get_Ans3(self):
        return self.Ans3.get()
    def set_Ans3(self, bool):
        self.Ans3.set(bool)

    def get_Ans4(self):
        return self.Ans4.get()
    def set_Ans4(self, bool):
        self.Ans4.set(bool)

#-----------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

    def on_Quit_click(self):
        """
        Handle on_Quit_click event
        Procedure: Exit/Close program
        """
        self.root.destroy()

    # No additional code necessarily needed for clicks
        # Avoids double assignment then
    def on_A_1_click(self):
        """
        Handle on_A_1_click event
        """
        pass
    def on_A_2_click(self):
        """
        Handle on_A_2_click event
        """
        pass
    def on_A_3_click(self):
        """
        Handle on_A_3_click event
        """
        pass
    def on_A_4_click(self):
        """
        Handle on_A_4_click event
        """
        pass

    def on_Clear_Ans_click(self):
        """
        Handle on_Clear_Ans_click event
        Function: Reset all selected answers to unchecked answers
        """
        self.set_Ans1(False)
        self.set_Ans2(False)
        self.set_Ans3(False)
        self.set_Ans4(False)

    def on_Submit_click(self):
        """
        Handle on_Submit_click event
        TODO: Implement code here
        """
        # Output all states of answers
        print(f"A1:{self.get_Ans1()}, A2:{self.get_Ans2()}, A3:{self.get_Ans3()}, A4:{self.get_Ans4()}")

#-----------------------------------------------------------------
    # ==========================================
    # Update Handlers - Implement direct logic for updates
    # ==========================================
    def update_question(self, new_Question):
        self.Question_Area.config(text=new_Question)

    def update_Ans1_Text(self, Ans1_Text):
        self.A_1.config(text=Ans1_Text)

    def update_Ans2_Text(self, Ans2_Text):
        self.A_2.config(text=Ans2_Text)

    def update_Ans3_Text(self, Ans3_Text):
        self.A_3.config(text=Ans3_Text)

    def update_Ans4_Text(self, Ans4_Text):
        self.A_4.config(text=Ans4_Text)

#-----------------------------------------------------------------

if __name__ == "__main__":
    print(f"TKinter Version {tk.TkVersion}")
    root = tk.Tk()
    app = Q_Page(root)
    root.mainloop()
