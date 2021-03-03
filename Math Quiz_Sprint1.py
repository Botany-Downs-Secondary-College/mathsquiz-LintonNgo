#Welcome.py 
#First screen to inform users about the programme
#L.Ngo Feb 21 
from tkinter import* 
from tkinter import ttk 
#Parent class 
class MathQuiz: 
    def __init__ (self,parent): 
        '''Widgets for Welcome Frame''' 
        self.Welcome = Frame(parent) 
        self.Welcome.grid(row=0, column=0) 
        
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic")) .grid(columnspan = 2) #Lable spans over two columns 
        self.NextButton = ttk.Button(self.Welcome, text = 'Next')
        self.NextButton.grid(row = 8, column = 1) 
#Main routine' 
if __name__== "__main__": 
    root =Tk() 
    frames = MathQuiz(root)
    root.title("Quiz") 
    root.mainloop()
 