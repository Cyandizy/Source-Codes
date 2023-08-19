import tkinter as tk
from tkinter import ttk
import math
import datetime
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

def create_input_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    date_hint = ttk.Label(frame, text="DD")
    date_hint.grid(column=1, row=0, padx=10)

    month_hint = ttk.Label(frame, text="MM")
    month_hint.grid(column=2, row=0, padx=10)

    year_hint = ttk.Label(frame, text="YYYY")
    year_hint.grid(column=3, row=0, padx=10)

    birthday_Label = ttk.Label(frame, text="Birthday:")
    birthday_Label.grid(column=0, row=1, padx=10, pady=10, sticky="E")

    global birthday_date_input
    birthday_date_input = ttk.Entry(frame, width=2)
    birthday_date_input.grid(column=1, row=1, padx=10)

    global birthday_month_input
    birthday_month_input = ttk.Entry(frame, width=2)
    birthday_month_input.grid(column=2, row=1, padx=10)

    global birthday_year_input
    birthday_year_input = ttk.Entry(frame, width=4)
    birthday_year_input.grid(column=3, row=1, padx=10)

    today_Label = ttk.Label(frame, text="Today:")
    today_Label.grid(column=0, row=2, padx=10, pady=10, sticky="E")

    global today_date_input
    today_date_input = ttk.Entry(frame, width=2)
    today_date_input.grid(column=1, row=2, padx=10)

    global today_month_input
    today_month_input = ttk.Entry(frame, width=2)
    today_month_input.grid(column=2, row=2, padx=10)

    global today_year_input
    today_year_input = ttk.Entry(frame, width=4)
    today_year_input.grid(column=3, row=2, padx=10)

    return frame


def store_value_and_calculate():
    try:

        birthday_date_Length = len(birthday_date_input.get())
        birthday_month_Length = len(birthday_month_input.get())
        birthday_year_Length = len(birthday_year_input.get())
        today_date_Length = len(today_date_input.get())
        today_month_Length = len(today_month_input.get())
        today_year_Length = len(today_year_input.get())

        if birthday_date_Length > 2 or birthday_month_Length > 2 or birthday_year_Length > 4 or today_date_Length > 2 or today_month_Length > 2 or today_year_Length > 4:

            result_Label.config(text="error")
            print("error")

        else:

            birthday_date = int(birthday_date_input.get())
            birthday_month = int(birthday_month_input.get())
            birthday_year = int(birthday_year_input.get())
            today_date = int(today_date_input.get())
            today_month = int(today_month_input.get())
            today_year = int(today_year_input.get())

            if birthday_date > 31 or birthday_month > 12 or today_date > 31 or today_month > 12:

                result_Label.config(text="error")
                print("error")

            else:

                total_birthday_day = birthday_date + birthday_month*30.4375 + birthday_year*365.25
                total_today_day = today_date + today_month*30.4375 + today_year*365.25
                total_day = total_today_day - total_birthday_day
                age_year = (total_day/30.4375)//12
                age_month = (total_day % 365.25)//30.4375
                age_day = total_day % 30.4375
                age_hour = str(age_day).rsplit(".", 1)
                age_hour = float("0." + age_hour[1])*24

                calculated_result = f"{math.floor(age_year)} Year(s) {math.floor(age_month)} Month(s)\n {math.floor(age_day)} Day(s) {math.floor(age_hour)} Hour(s)"
                result_Label.config(text=calculated_result)
                print(calculated_result)

    except:

        print("error")


def create_button_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=2)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    def clear(type):
        if type == "all":
            birthday_date_input.delete(0, "end")
            birthday_month_input.delete(0, "end")
            birthday_year_input.delete(0, "end")
            today_date_input.delete(0, "end")
            today_month_input.delete(0, "end")
            today_year_input.delete(0, "end")
        else:
            today_date_input.delete(0, "end")
            today_month_input.delete(0, "end")
            today_year_input.delete(0, "end")

    calculate_button = ttk.Button(
        frame, text="Calculate", command=store_value_and_calculate)
    calculate_button.grid(column=0, row=0, padx=10, pady=5, sticky="W")

    clear_button = ttk.Button(
        frame, text="Clear", command=lambda: [clear("all")])
    clear_button.grid(column=0, row=1, padx=10, pady=5, sticky="W")

    current_date = str(datetime.datetime.now())[8:10]
    current_month = str(datetime.datetime.now())[5:7]
    current_year = str(datetime.datetime.now())[0:4]

    def use_current_date_function():

        clear("current date")
        today_date_input.insert(0, current_date)
        today_month_input.insert(0, current_month)
        today_year_input.insert(0, current_year)

    use_current_date_button = ttk.Button(
        frame, text="Use Current Date", command=use_current_date_function,)
    use_current_date_button.grid(column=0, row=2, padx=10, pady=5, sticky="W")

    return frame


def create_result_frame(container):
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=2)
    frame.rowconfigure(0, weight=1)

    global result_Label
    result_Label = ttk.Label(frame, text="")
    result_Label.grid(column=0, row=0, padx=10, pady=10)

    return frame


def create_main_window():

    root = tk.Tk()
    root.title("Age Calculator")
    root.resizable(0, 0)
    root.columnconfigure(0, weight=6)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0, sticky="W")

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0, sticky="E")

    result_frame = create_result_frame(root)
    result_frame.grid(column=0, row=1, sticky="W", padx=10)

    root.mainloop()


create_main_window()
