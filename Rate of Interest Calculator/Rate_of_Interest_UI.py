import tkinter as tk
from tkinter import ttk
import math
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

type_1_selected = False
type_2_selected = False
type_3_selected = False
info_screen = False

def convert_and_calculate():
    if type_1_selected == True:
        
        total_collected = total_input.get()
        print(f"Total = {total_collected}")

        current_collected = current_input.get()
        print(f"Current = {current_collected}")

        rate_collected = rate_input.get()
        print(f"Rate = {rate_collected}")

        n_collected = n_input.get()
        print(f"n = {n_collected}")

        k_collected = k_input.get()
        print(f"k = {k_collected}")

        if total_collected == "?" or total_collected == "":
            #Floatize
            F_current = float(current_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            powered_rate = math.pow(1 + rate_DIVby_k, power)
            result = F_current*powered_rate
            #Output
            total_input.insert(0, result)
            print(result)

        elif current_collected == "?" or current_collected == "":
            #Floatize
            F_total = float(total_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            powered_rate = math.pow(1 + rate_DIVby_k, power)
            result = F_total/powered_rate
            #Output
            current_input.insert(0, result)
            print(result)

        elif rate_collected == "?" or rate_collected == "":
            #Floatize
            F_total = float(total_collected)
            F_current = float(current_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            #Calculate
            total_DIVby_current = F_total/F_current
            power = F_n*F_k
            root_of_n_tDc = total_DIVby_current**(1/power)
            result = (root_of_n_tDc - 1)*F_k
            result = result*100
            #Output
            rate_input.insert(0, result)
            print(result)
        
        elif n_collected == "?" or n_collected == "":
            #Floatize
            F_total = float(total_collected)
            F_current = float(current_collected)
            F_k = float(k_collected)
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            total_DIVby_current = F_total/F_current
            rate_DIVby_k = F_rate/F_k
            rDk_plus_one = rate_DIVby_k + 1
            result = (math.log(total_DIVby_current, rDk_plus_one))/F_k
            #Output
            n_input.insert(0, result)
            print(result)

        elif k_collected == "?" or k_collected == "":
            #Output
            k_input.insert(0, "Error")
            print("Could not find the result")

    elif type_2_selected == True:
        total_collected = total_input.get()
        print(f"Total = {total_collected}")

        recurring_collected = recurring_input.get()
        print(f"Recurring = {recurring_collected}")

        rate_collected = rate_input.get()
        print(f"Rate = {rate_collected}")

        n_collected = n_input.get()
        print(f"n = {n_collected}")

        k_collected = k_input.get()
        print(f"k = {k_collected}")

        if total_collected == "?" or total_collected == "":
            #Floatize
            F_recurring = float(recurring_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            #Rate
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = rate_DIVby_k + 1
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            recurring_rpo_prmo = F_recurring*rDk_plus_one*powered_rpo_minus_one
            result = recurring_rpo_prmo/rate_DIVby_k
            #Output
            total_input.insert(0, result)
            print(result)
        
        elif recurring_collected == "?" or recurring_collected == "":
            #Floatize
            F_total = float(total_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            #Rate
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = 1 + rate_DIVby_k
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            recurring_rpo_prmo = rDk_plus_one*powered_rpo_minus_one
            result = F_total*rate_DIVby_k/recurring_rpo_prmo
            #Output
            recurring_input.insert(0, result)
            print(result)
        
        elif rate_collected == "?" or rate_collected == "":
            #Output
            rate_input.insert(0, "Error")
            print("Could not find the result")
        
        elif n_collected == "?" or rate_collected == "":
            #Floatize
            F_total = float(total_collected)
            F_recurring = float(recurring_collected)
            F_k = float(k_collected)
            #Rate
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            rDk_plus_one = rate_DIVby_k + 1
            recurring_times_rpo = F_recurring*rDk_plus_one
            total_times_rDk = F_total*rate_DIVby_k
            ttr_DIVby_rtr = total_times_rDk/recurring_times_rpo
            tDr_plus_one = ttr_DIVby_rtr + 1
            result = math.log(tDr_plus_one, rDk_plus_one)/F_k
            #Output
            n_input.insert(0, result)
            print(result)
        
        elif k_collected == "?" or k_collected == "":
            #Output
            k_input.insert(0, "Error")
            print("Could not find the result")
        
    elif type_3_selected == True:

        total_collected = total_input.get()
        print(f"Total = {total_collected}")

        recurring_collected = recurring_input.get()
        print(f"Recurring = {recurring_collected}")

        rate_collected = rate_input.get()
        print(f"Rate = {rate_collected}")

        n_collected = n_input.get()
        print(f"n = {n_collected}")

        k_collected = k_input.get()
        print(f"k = {k_collected}")

        if total_collected == "?" or total_collected == "":
            #Floatize
            F_recurring = float(recurring_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            #Rate
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = rate_DIVby_k + 1
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo-  1
            recurring_rpo_prmo = F_recurring*powered_rpo_minus_one
            result = recurring_rpo_prmo/rate_DIVby_k
            #Output
            total_input.insert(0, result)
            print(result)
        
        elif recurring_collected == "?" or recurring_collected == "":
            # Floatize
            F_total = float(total_collected)
            F_n = float(n_collected)
            F_k = float(k_collected)
            # Rate
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            # Calculate
            rate_DIVby_k = F_rate/F_k
            power = F_n*F_k
            rDk_plus_one = 1 + rate_DIVby_k
            powered_rpo = rDk_plus_one**power
            powered_rpo_minus_one = powered_rpo - 1
            result = F_total*rate_DIVby_k/powered_rpo_minus_one
            #Output
            recurring_input.insert(0, result)
            print(result)
        
        elif rate_collected == "?" or rate_collected == "":
            #Output
            rate_input.insert(0, "Error")
            print("Could not find the result")
        
        elif n_collected == "?" or n_collected == "":
            #Floatize
            F_total = float(total_collected)
            F_recurring = float(recurring_collected)
            F_k = float(k_collected)
            #Rate
            F_rate = float(rate_collected.replace("%",""))
            F_rate = F_rate/100
            #Calculate
            rate_DIVby_k = F_rate/F_k
            rDk_plus_one = rate_DIVby_k + 1
            total_times_rDk = F_total*rate_DIVby_k
            ttr_DIVby_recurring = total_times_rDk/F_recurring
            tDr_plus_one = ttr_DIVby_recurring + 1
            result = math.log(tDr_plus_one, rDk_plus_one)/F_k
            #Output
            n_input.insert(0, result)
            print(result)
        
        elif k_collected == "?" or k_collected == "":
            #Output
            k_input.insert(0, "Error")
            print("Could not find the result")

def create_option_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=4)

    SelectTypeLabel = ttk.Label(frame, text = "Select Solutions").grid(column=0, row=0, padx=5, pady=5)

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

    #Type 1
    Type_1 = ttk.Button(frame, text = "Current Account Compound Interest", command=lambda:[Switch_R_to_P(), Type_on(1)])
    Type_1.grid(column=0, row=1, sticky=tk.W, padx=5, pady=2)

    #Type 2
    Type_2 = ttk.Button(frame, text = "Recurring Deposite Compound Interest (at the BEGINNING of n)", command=lambda:[Switch_P_to_R(), Type_on(2)])
    Type_2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=2)

    #Type 3
    Type_3 = ttk.Button(frame, text = "Recurring Deposite Compound Interest (at the END of n)", command=lambda:[Switch_P_to_R(), Type_on(3)])
    Type_3.grid(column=0, row=3, sticky=tk.W, padx=5, pady=2)

    #Input Label
    input_frame_Label = ttk.Label(frame, text = "Input Variables")
    input_frame_Label.grid(column=0, row=4, padx=5, pady=5)

    return frame


def create_input_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=2)
    frame.columnconfigure(2, weight=2)
    
    #Total
    global total_input
    total = ttk.Label(frame, text = "S").grid(column=0, row=0, sticky=tk.W, padx=5)
    total_input = ttk.Entry(frame, width=20)
    total_input.focus()
    total_input.grid(column=2, row=0)
    total_Label = ttk.Label(frame, text = "Total").grid(column=3, row=0, sticky=tk.W, padx=5)


    #Current
    global current
    global current_input
    global current_Label
    current = ttk.Label(frame, text = "P")
    current.grid(column=0, row=1, sticky=tk.W, padx=5)
    current_input = ttk.Entry(frame, width=20)
    current_input.grid(column=2, row=1, sticky=tk.W)
    current_Label = ttk.Label(frame, text = "Current")
    current_Label.grid(column=3, row=1, sticky=tk.W, padx=5)

    #Recurring
    global recurring
    global recurring_input
    global recurring_Label
    recurring = ttk.Label(frame, text = "R")
    recurring.grid_forget()
    recurring_input = ttk.Entry(frame, width=20)
    recurring_input.grid_forget()
    recurring_Label = ttk.Label(frame, text = "Recurring")
    recurring_Label.grid_forget()

    #Rate
    global rate_input
    rate = ttk.Label(frame, text = "r").grid(column=0, row = 2, sticky=tk.W, padx=5)
    rate_input = ttk.Entry(frame, width=20)
    rate_input.grid(column=2, row=2, sticky=tk.W)
    rate_Label = ttk.Label(frame, text = "Rate").grid(column=3, row=2, sticky=tk.W, padx=5)

    #n
    global n_input
    n = ttk.Label(frame, text= "n").grid(column=0, row = 3, stick=tk.W, padx=5)
    n_input = ttk.Entry(frame, width=20)
    n_input.grid(column=2, row=3, sticky=tk.W)
    n_Label = ttk.Label(frame, text = "Number of years").grid(column=3, row=3, sticky=tk.W, padx=5)

    #k
    global k_input
    k = ttk.Label(frame, text= "k").grid(column=0, row = 4, stick=tk.W, padx=5)
    k_input = ttk.Entry(frame, width=20)
    k_input.grid(column=2, row=4, sticky=tk.W)
    k_Label = ttk.Label(frame, text = '"k" times per year').grid(column=3, row=4, sticky=tk.W, padx=5)

    #Calculate
    calculate_button = ttk.Button(frame, text= "Calculate", command=convert_and_calculate)
    calculate_button.grid(column=2, row=5, pady=5)

    def info():
        global info_screen
        if info_screen == False:
            info_frame.grid(column=0, row=2, sticky=tk.W, padx=5)
            info_screen = True
        elif info_screen == True:
            info_frame.grid_forget()
            info_screen = False

    #Info button
    info_frame_button = ttk.Button(frame, text = "Help", command=info)
    info_frame_button.grid(column=4, row=5, sticky='E')

    return frame

def Switch_P_to_R():
        current.grid_forget()
        current_input.grid_forget()
        current_Label.grid_forget()
        recurring.grid(column=0, row=1, sticky=tk.W, padx=5)
        recurring_input.grid(column=2, row=1, sticky=tk.W)
        recurring_Label.grid(column=3, row=1, sticky=tk.W, padx=5)

def Switch_R_to_P():
        recurring.grid_forget()
        recurring_input.grid_forget()
        recurring_Label.grid_forget()
        current.grid(column=0, row=1, sticky=tk.W, padx=5)
        current_input.grid(column=2, row=1, sticky=tk.W)
        current_Label.grid(column=3, row=1, sticky=tk.W, padx=5)

def create_info_frame(container):
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=4)
    #Help screen
    info_Label_1 = ttk.Label(frame, text = "Due to the complicatedness of formulae, some of variable ")
    info_Label_1.grid(column=0, row=0, sticky='W')
    info_Label_2 = ttk.Label(frame, text = "here cannot be calculated and will be displayed as 'error'.")
    info_Label_2.grid(column=0, row=1, sticky='W')
    info_Label_3 = ttk.Label(frame, text = "I strongly apologize.")
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
