import tkinter as tk
from tkinter import ttk

import pandas as pd

import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Data
data = pd.read_csv('placeholder.csv')

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

data_view.pack(side="left",fill="y")
data_view_scrollbar.pack(side="left", fill="y")

# Plot
scatter_plot = Figure(figsize=(6, 6))
ax = scatter_plot.subplots()
sns.scatterplot(data=data.iloc[:,[1,3]], ax=ax)

canvas = FigureCanvasTkAgg(figure=scatter_plot, master=window)
canvas.draw()

# TODO: Change pack to grid
canvas.get_tk_widget().pack(side="right", before=data_view)

# Input
# Run
window.mainloop()