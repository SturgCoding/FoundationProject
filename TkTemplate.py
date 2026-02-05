    # ==========================================
    # Required imports - tkinter plus dependencies
    # ==========================================

import tkinter as tk
from tkinter import ttk

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
            font=("Courier New", 15),
            textvariable = question_no(),
            bg="#ffffff",
            fg="#000000"
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
            text="{Ans}",
            variable=self.Ans1,
            command=self.on_A_1_click
        )
        self.A_1.place(x=380, y=260)

        # A_2
        self.A_2 = tk.Checkbutton(
            self.root,
            text="{Ans}",
            variable=self.Ans2,
            command=self.on_A_2_click
        )
        self.A_2.place(x=380, y=300)

        # A_3
        self.A_3 = tk.Checkbutton(
            self.root,
            text="{Ans}",
            variable=self.Ans3,
            command=self.on_A_3_click
        )
        self.A_3.place(x=380, y=340)

        # A_4
        self.A_4 = tk.Checkbutton(
            self.root,
            text="{Ans}",
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
        return self.Ans1
    def set_Ans1(self, bool):
        self.Ans1 = bool

    def get_Ans2(self):
        return self.Ans2
    def set_Ans2(self, bool):
        self.Ans2 = bool

    def get_Ans3(self):
        return self.Ans3
    def set_Ans3(self, bool):
        self.Ans3 = bool

    def get_Ans4(self):
        return self.Ans3
    def set_Ans4(self, bool):
        self.Ans4 = bool

#-----------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

    def on_Quit_click(self):
        """
        Handle on_Quit_click event
        Procedure: Exit program
        """
        self.root.destroy()

    def on_A_1_click(self):
        """
        Handle on_A_1_click event
        """
        self.Ans1 = not self.Ans1

    def on_A_2_click(self):
        """
        Handle on_A_2_click event
        """
        self.Ans2 = not self.Ans2

    def on_A_3_click(self):
        """
        Handle on_A_3_click event
        """
        self.Ans3 = not self.Ans3

    def on_A_4_click(self):
        """
        Handle on_A_4_click event
        """
        self.Ans4 = not self.Ans4

    def on_Clear_Ans_click(self):
        """
        Handle on_Clear_Ans_click event
        Function: Reset all selected answers to unchecked answers
        """
        Q_Page.set_Ans1(self, False)
        Q_Page.set_Ans2(self, False)
        Q_Page.set_Ans3(self, False)
        Q_Page.set_Ans4(self, False)

    def on_Submit_click(self):
        """
        Handle on_Submit_click event
        """
        submitted = [Q_Page.get_Ans1(self),Q_Page.get_Ans2(self),Q_Page.get_Ans3(self),Q_Page.get_Ans4(self)]
        check_answers(submitted)

#-----------------------------------------------------------------
    # ==========================================
    # Event Handlers - Implement event logic
    # ==========================================

def question_no(question=0):
    """
    Handle Q_number event
    Procedure: Find the question from question number
    Defaults: question = 0 else passed val, question_text = "" blank if question fails
    """
    question_text = "" #Default to blank
    try:
        question_text = find_question(question)
    except TypeError:
        pass
    finally:
        return question_text

def find_question(question):
    QUESTION_LIST = ["What is the formula for Voltage?","N/A","N/A"]
    return QUESTION_LIST[question]

def check_answers(answers):
    """
    Handle check_answers event
    Function: Look at all selected answers and compare
    TODO: Implement your logic here
    """
    #Test code
    print(answers)

#-----------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = Q_Page(root)
    root.mainloop()
