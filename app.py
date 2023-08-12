import tkinter as tk
from tkinter import ttk
import pandas as pd

# Data
data = pd.read_csv('placeholder.csv')
print(list(data.iloc[1]))

# Main window
window = tk.Tk()
window.title('EDA')
#window.geometry('300x300')

# Title
title_label = ttk.Label(master=window, text='Exploratory Data Analysis')
title_label.pack()

# Data view
data_view_scrollbar = ttk.Scrollbar(master=window)

data_view = ttk.Treeview(master=window, columns=list(data.columns), show="headings", yscrollcommand=data_view_scrollbar.set)
for i, heading in enumerate(list(data.columns)):
    data_view.heading(i, text=heading)
for index, row in data.iterrows():
    data_view.insert(parent="", index="end", values=row.to_list())

data_view_scrollbar.config(command=data_view.yview)

# TODO: Scrollbar stick to data_view
data_view.pack(side="left",fill="both")
data_view_scrollbar.pack(side="right", fill="y")

# Input
# Run
window.mainloop()