from tkinter import * 
class outline:
	def __init__(self, root):
		self.root = root
		self.root.title('Quadratic Equation Solver App')
		# self.root.geometry("360*360")

		title = Label(self.root, text = "Quadratic Equation Solver App", bd =10,
			relief = GROOVE, pady=10, font=("times new roman", 30, "bold")).pack(fill=X)

		eqFrame = Frame(self.root, bd = 10, relief=GROOVE)
		eqFrame.place(x=20, y=100, height=200)
		eTitle = Label(eqFrame, text ='Please fill the required fields',
			font = ("times new roman", 20, "bold")).grid(row =0, columnspan=4, pady=20 )

		self.coef1 = StringVar()	
root = Tk()
ob  = outline(root)
root.mainloop()