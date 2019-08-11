import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk() # Create instance
window.title('图片处理工具') # Add a title
window.geometry('800x400')

tabControl = ttk.Notebook(window) # Create Tab Control
tab1 = ttk.Frame(tabControl) # Create a Tab
tabControl.add(tab1, text='Tab 1') # Add the Tab
tab2 = ttk.Frame(tabControl) # Create second Tab
tabControl.add(tab2, text='Tab 2') # Add second Tab
tabControl.pack(expand=1, fill='both') # Pack to make visible

# LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Label using mighty as the parent
a_label = ttk.Label(mighty, text=' Enter a number: ')
a_label.grid(column=0, row=0, sticky='W')

# Modified Button click Event Function
def click_me():
	action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W') # column 0

# Adding a Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1, sticky='W') # change column to 2

ttk.Label(mighty, text='Choose a number:').grid(column=1, row=0, sticky='W')

number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1, sticky='W') # Combobox in column 1
number_chosen.current(4)

# Using a scrlled text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

window.mainloop()