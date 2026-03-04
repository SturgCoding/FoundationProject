import tkinter as tk
import threading
from src.gui import Bean_Can

def get_and_get_Gravity_value(instance):
    temp_store = []
    for i in range(-10,60,1): # TEST VALUES FROM -10 -> 100
        temp_store.append(Bean_Can.get_Gravity_value(bean))
        Bean_Can.set_Gravity_value(bean, i)
        temp_store.append(Bean_Can.get_Gravity_value(bean))
    min_val, max_val = -9.81, 50
    if all(min_val <= x <= max_val for x in temp_store):
        print("All elements are within the specified range")
    else:
        print("Value out of range within test criteria")

def gui_tests(bean):
    get_and_get_Gravity_value(bean)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()          # hide the window

    bean = Bean_Can(root)

    # run tests in background
    threading.Thread(
        target=gui_tests,
        args=(bean,),
        daemon=True
    ).start()

    root.mainloop()