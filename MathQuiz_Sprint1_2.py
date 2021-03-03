from tkinter import* 
class MathsQuiz:
    def __init__ (self,parent): 
        '''Widgets for Welcome Frame'''
        self.Welcome = Frame(parent) 
        self.Welcome.grid(row=0, column=0) 
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic")) 
        self.TitleLabel.grid(columnspan = 2) 
        self.NextButton = Button(self.Welcome, text = 'Next') 
        self.NextButton.grid(row = 8, column = 1) 
        '''Widgets for Question Frame'''
        self.Questions - Frame(parent) 
        self.Questions.grid(row=0, column=1) 
        
        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic")) 
        self.QuestionsLabel.grid(columnspan = 2) 
        
        self.HomeButton = Button(self.Questions, text = 'Next')
        self.HomeButton.grid(row = 8, column = 1) 

if __name__ == " __main__ ": 
    root =Tk() 
    frames = MathsQuiz(root) 
    root.title("Quiz")
    root.mainloop() 
