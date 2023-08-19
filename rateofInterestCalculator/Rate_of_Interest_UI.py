import tkinter as tk
from tkinter import ttk
import math
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

# These variables are used to keep track of whether a type of calculation has been selected.
type_1_selected = False
type_2_selected = False
type_3_selected = False

# This variable is used to keep track of whether the information screen is currently displayed.
info_screen = False


def convert_and_calculate():
    if type_1_selected == True:

        input_collection = {
            "total": total_input.get(),
            "current": current_input.get(),
            "rate": rate_input.get(),
            "n": n_input.get(),
            "k": k_input.get()
        }

        print(f"Total = {input_collection['total']}")
        print(f"Current = {input_collection['current']}")
        print(f"Rate = {input_collection['rate']}")
        print(f"n = {input_collection['n']}")
        print(f"k = {input_collection['k']}")

        if input_collection['total'] == "?" or input_collection['total'] == "":
            F_current = float(input_collection['current'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            powered_rate = math.pow(1 + rate_DIVby_k, power)
            result = F_current*powered_rate
            # Output
            total_input.insert(0, result)
            print(result)

        elif input_collection['current'] == "?" or input_collection['current'] == "":

            F_total = float(input_collection['total'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            powered_rate = math.pow(1 + rate_DIVby_k, power)
            result = F_total/powered_rate
            # Output
            current_input.insert(0, result)
            print(result)

        elif input_collection['rate'] == "?" or input_collection['rate'] == "":

            F_total = float(input_collection['total'])
            F_current = float(input_collection['current'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            # Calculate
            total_DIVby_current = F_total/F_current
            power = F_n*F_k
            root_of_n_tDc = total_DIVby_current**(1/power)
            result = (root_of_n_tDc - 1)*F_k
            result = result*100
            # Output
            rate_input.insert(0, result)
            print(result)

        elif input_collection['n'] == "?" or input_collection['n'] == "":

            F_total = float(input_collection['total'])
            F_current = float(input_collection['current'])
            F_k = float(input_collection['k'])
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            total_DIVby_current = F_total/F_current
            rate_DIVby_k = F_rate/F_k
            rDk_plus_one = rate_DIVby_k + 1
            result = (math.log(total_DIVby_current, rDk_plus_one))/F_k
            # Output
            n_input.insert(0, result)
            print(result)

        elif input_collection['k'] == "?" or input_collection['k'] == "":
            # Output
            k_input.insert(0, "Error")
            print("Could not find the result")

    elif type_2_selected == True:

        input_collection = {
            "total": total_input.get(),
            "recurring": recurring_input.get(),
            "rate": rate_input.get(),
            "n": n_input.get(),
            "k": k_input.get()
        }

        print(f"Total = {input_collection['total']}")
        print(f"Recurring = {input_collection['recurring']}")
        print(f"Rate = {input_collection['rate']}")
        print(f"n = {input_collection['n']}")
        print(f"k = {input_collection['k']}")

        if input_collection['total'] == "?" or input_collection['total'] == "":

            F_recurring = float(input_collection['recurring'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            # Rate
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = rate_DIVby_k + 1
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            recurring_rpo_prmo = F_recurring*rDk_plus_one*powered_rpo_minus_one
            result = recurring_rpo_prmo/rate_DIVby_k
            # Output
            total_input.insert(0, result)
            print(result)

        elif input_collection['recurring'] == "?" or input_collection['recurring'] == "":

            F_total = float(input_collection['total'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            # Rate
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = 1 + rate_DIVby_k
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            recurring_rpo_prmo = rDk_plus_one*powered_rpo_minus_one
            result = F_total*rate_DIVby_k/recurring_rpo_prmo
            # Output
            recurring_input.insert(0, result)
            print(result)

        elif input_collection['rate'] == "?" or input_collection['rate'] == "":
            # Output
            rate_input.insert(0, "Error")
            print("Could not find the result")

        elif input_collection['n'] == "?" or input_collection['rate'] == "":

            F_total = float(input_collection['total'])
            F_recurring = float(input_collection['recurring'])
            F_k = float(input_collection['k'])
            # Rate
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            rDk_plus_one = rate_DIVby_k + 1
            recurring_times_rpo = F_recurring*rDk_plus_one
            total_times_rDk = F_total*rate_DIVby_k
            ttr_DIVby_rtr = total_times_rDk/recurring_times_rpo
            tDr_plus_one = ttr_DIVby_rtr + 1
            result = math.log(tDr_plus_one, rDk_plus_one)/F_k
            # Output
            n_input.insert(0, result)
            print(result)

        elif input_collection['k'] == "?" or input_collection['k'] == "":
            # Output
            k_input.insert(0, "Error")
            print("Could not find the result")

    elif type_3_selected == True:

        input_collection = {
            "total": total_input.get(),
            "recurring": recurring_input.get(),
            "rate": rate_input.get(),
            "n": n_input.get(),
            "k": k_input.get()
        }

        print(f"Total = {input_collection['total']}")
        print(f"Recurring = {input_collection['recurring']}")
        print(f"Rate = {input_collection['rate']}")
        print(f"n = {input_collection['n']}")
        print(f"k = {input_collection['k']}")

        if input_collection['total'] == "?" or input_collection['total'] == "":

            F_recurring = float(input_collection['recurring'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            # Rate
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = rate_DIVby_k + 1
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            recurring_rpo_prmo = F_recurring*powered_rpo_minus_one
            result = recurring_rpo_prmo/rate_DIVby_k
            # Output
            total_input.insert(0, result)
            print(result)

        elif input_collection['recurring'] == "?" or input_collection['recurring'] == "":
            # Floatize
            F_total = float(input_collection['total'])
            F_n = float(input_collection['n'])
            F_k = float(input_collection['k'])
            # Rate
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = 1 + rate_DIVby_k
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            result = F_total*rate_DIVby_k/powered_rpo_minus_one
            # Output
            recurring_input.insert(0, result)
            print(result)

        elif input_collection['rate'] == "?" or input_collection['rate'] == "":
            # Output
            rate_input.insert(0, "Error")
            print("Could not find the result")

        elif input_collection['n'] == "?" or input_collection['n'] == "":

            F_total = float(input_collection['total'])
            F_recurring = float(input_collection['recurring'])
            F_k = float(input_collection['k'])
            # Rate
            F_rate = float(input_collection['rate'].replace("%", ""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            rDk_plus_one = rate_DIVby_k + 1
            total_times_rDk = F_total*rate_DIVby_k
            ttr_DIVby_recurring = total_times_rDk/F_recurring
            tDr_plus_one = ttr_DIVby_recurring + 1
            result = math.log(tDr_plus_one, rDk_plus_one)/F_k
            # Output
            n_input.insert(0, result)
            print(result)

        elif input_collection['k'] == "?" or input_collection['k'] == "":
            # Output
            k_input.insert(0, "Error")
            print("Could not find the result")


def create_option_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=4)

    select_type_label = ttk.Label(frame, text="Select Solutions").grid(
        column=0, row=0, padx=5, pady=5)

    def Type_on(type):
        global type_1_selected
        global type_2_selected
        global type_3_selected
        if type == 1:
            input_frame.grid(column=0, row=1)
            type_1_selected = True
            type_2_selected = False
            type_3_selected = False
            print("Type1 = True")

        elif type == 2:
            input_frame.grid(column=0, row=1)
            type_1_selected = False
            type_2_selected = True
            type_3_selected = False
            print("Type2 = True")

        elif type == 3:
            input_frame.grid(column=0, row=1)
            type_1_selected = False
            type_2_selected = False
            type_3_selected = True
            print("Type3 = True")

    # Type 1
    Type_1 = ttk.Button(frame, text="Current Account Compound Interest",
                        command=lambda: [Switch_R_to_P(), Type_on(1)])
    Type_1.grid(column=0, row=1, sticky=tk.W, padx=5, pady=2)

    # Type 2
    Type_2 = ttk.Button(frame, text="Recurring Deposite Compound Interest (at the BEGINNING of n)",
                        command=lambda: [Switch_P_to_R(), Type_on(2)])
    Type_2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=2)

    # Type 3
    Type_3 = ttk.Button(frame, text="Recurring Deposite Compound Interest (at the END of n)",
                        command=lambda: [Switch_P_to_R(), Type_on(3)])
    Type_3.grid(column=0, row=3, sticky=tk.W, padx=5, pady=2)

    # Input Label
    input_frame_Label = ttk.Label(frame, text="Input Variables")
    input_frame_Label.grid(column=0, row=4, padx=5, pady=5)

    return frame


def create_input_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=2)
    frame.columnconfigure(2, weight=2)

    # Total
    global total_input
    total_abbr = ttk.Label(frame, text="S").grid(
        column=0, row=0, sticky=tk.W, padx=5)
    total_input = ttk.Entry(frame, width=20)
    total_input.focus()
    total_input.grid(column=2, row=0)
    total_Label = ttk.Label(frame, text="Total").grid(
        column=3, row=0, sticky=tk.W, padx=5)

    # Current
    global current_abbr
    global current_input
    global current_Label
    current_abbr = ttk.Label(frame, text="P")
    current_abbr.grid(column=0, row=1, sticky=tk.W, padx=5)
    current_input = ttk.Entry(frame, width=20)
    current_input.grid(column=2, row=1, sticky=tk.W)
    current_Label = ttk.Label(frame, text="Current")
    current_Label.grid(column=3, row=1, sticky=tk.W, padx=5)

    # Recurring
    global recurring_abbr
    global recurring_input
    global recurring_Label
    recurring_abbr = ttk.Label(frame, text="R")
    recurring_abbr.grid_forget()
    recurring_input = ttk.Entry(frame, width=20)
    recurring_input.grid_forget()
    recurring_Label = ttk.Label(frame, text="Recurring")
    recurring_Label.grid_forget()

    # Rate
    global rate_input
    rate_abbr = ttk.Label(frame, text="r").grid(
        column=0, row=2, sticky=tk.W, padx=5)
    rate_input = ttk.Entry(frame, width=20)
    rate_input.grid(column=2, row=2, sticky=tk.W)
    rate_Label = ttk.Label(frame, text="Rate").grid(
        column=3, row=2, sticky=tk.W, padx=5)

    # n
    global n_input
    n_abbr = ttk.Label(frame, text="n").grid(
        column=0, row=3, stick=tk.W, padx=5)
    n_input = ttk.Entry(frame, width=20)
    n_input.grid(column=2, row=3, sticky=tk.W)
    n_Label = ttk.Label(frame, text="Number of years").grid(
        column=3, row=3, sticky=tk.W, padx=5)

    # k
    global k_input
    k_abbr = ttk.Label(frame, text="k").grid(
        column=0, row=4, stick=tk.W, padx=5)
    k_input = ttk.Entry(frame, width=20)
    k_input.grid(column=2, row=4, sticky=tk.W)
    k_Label = ttk.Label(frame, text='"k" times per year').grid(
        column=3, row=4, sticky=tk.W, padx=5)

    # Calculate
    calculate_button = ttk.Button(
        frame, text="Calculate", command=convert_and_calculate)
    calculate_button.grid(column=2, row=5, pady=5)

    def info():
        global info_screen
        if info_screen == False:
            info_frame.grid(column=0, row=2, sticky=tk.W, padx=5, pady=10)
            info_screen = True
        elif info_screen == True:
            info_frame.grid_forget()
            info_screen = False

    # Info button
    info_frame_button = ttk.Button(frame, text="Help", command=info)
    info_frame_button.grid(column=4, row=5, sticky='E')

    return frame


def Switch_P_to_R():
    current_abbr.grid_forget()
    current_input.grid_forget()
    current_Label.grid_forget()
    recurring_abbr.grid(column=0, row=1, sticky=tk.W, padx=5)
    recurring_input.grid(column=2, row=1, sticky=tk.W)
    recurring_Label.grid(column=3, row=1, sticky=tk.W, padx=5)


def Switch_R_to_P():
    recurring_abbr.grid_forget()
    recurring_input.grid_forget()
    recurring_Label.grid_forget()
    current_abbr.grid(column=0, row=1, sticky=tk.W, padx=5)
    current_input.grid(column=2, row=1, sticky=tk.W)
    current_Label.grid(column=3, row=1, sticky=tk.W, padx=5)


def create_info_frame(container):
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=4)
    # Help screen
    info_Label_1 = ttk.Label(
        frame, text="Due to limitations, some variables")
    info_Label_1.grid(column=0, row=0, sticky='W')
    info_Label_2 = ttk.Label(
        frame, text="here cannot be calculated and will be displayed as 'error'.")
    info_Label_2.grid(column=0, row=1, sticky='W')
    info_Label_3 = ttk.Label(frame, text="I strongly apologize.")
    info_Label_3.grid(column=0, row=2, sticky='W')
    return frame


def create_main_window():

    global input_frame
    global info_frame

    root = tk.Tk()
    root.title("Rate of Interest Calculator")
    root.resizable(0, 0)

    root.columnconfigure(0, weight=4)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    option_frame = create_option_frame(root)
    option_frame.grid(column=0, row=0)

    input_frame = create_input_frame(root)

    info_frame = create_info_frame(root)

    root.mainloop()


create_main_window()
