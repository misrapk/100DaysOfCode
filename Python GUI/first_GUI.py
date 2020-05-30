import tkinter as tk
from tkinter import ttk 
"""ttk --> themed tk. It improves our GUI's look and feel."""


win = tk.Tk()
win.title('Python GUI')

#disable resize
# win.resizable(False, False)  #prevent both x and y resizable 
"""(True, False) --> enable x-direction
	(False, True)  --> enable y-direction only
	"""
#add label
aLabel = ttk.Label(win, text = 'A label')
aLabel.grid(column=0, row=0)

#button click event
def clickMe():
	action.configure(text="** I have been Clicked! **")
	aLabel.configure(foreground = 'red')
	aLabel.configure(text = 'A red Label')

#add button
action = ttk.Button(win, text= "CLICK Me!", command = clickMe)
action.grid(column=1, row = 0)


win.mainloop()