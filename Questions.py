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
