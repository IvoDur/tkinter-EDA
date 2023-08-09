import tkinter as tk
from tkinter import ttk
import pandas as pd


data = pd.read_csv('placeholder.csv')

# Main window
window = tk.Tk()
window.title('EDA')
window.geometry('300x300')

# Title
title_label = ttk.Label(master=window, text='Exploratory Data Analysis')
title_label.pack()

# Input
# Run
window.mainloop()