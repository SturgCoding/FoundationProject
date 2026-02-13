"""
    File: Questions.py
    Project: Foundation-CompApps
    Purpose: To provide Questions and their Answers used within the project
"""

def question_no(question=0):
    """
    Handle Q_number event
    Procedure: Find the question from question number
    Defaults: question = 0 else passed val, question_text = "Initializing..."  if question fails
    TODO: Implement your logic here
    """
    pass

def find_question(question):
    QUESTION_LIST = ["What is the formula for Voltage?","N/A","N/A"]
    return QUESTION_LIST[question]

def check_answers(answers):
    """
    Handle check_answers event
    Function: Look at all selected answers and compare
    Logic: Passed by value a set/list of the selected answers, compare against the Question_List_Answers, return result
    TODO: Implement your logic here
    """
    #Test code
    print(answers)
