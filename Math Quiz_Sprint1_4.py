def show_Questions(self):
    try: 
    #Error checking for empty or non-text user entries for Name 
        if self.NameEntry.get() == "": 
            self.WarningLabel.configure(text = "Please enter name") 
            self.NameEntry.focus() 
            
        elif self.NameEntry.get().isalpha() == False: 
            self.WarningLabel.configure(text = "Pleasae enter text") 
            self.NameEntry.delete(0, END) 
            self.NameEntry. focus () 
            
            #Error checking for empty and age limit cases
        elif self.AgeEntry.get() == "": 
            self.WarningLabel.configure(text = "Please enter age") 
            self.AgeEntry.focus() 
            
        elif int(self.AgeEntry.get()) > 12: 
            self.WarningLabel.configure (text = "You are too old! ") 
            self.AgeEntry.delete(0, END) 
            self.AgeEntry.focus() 
        elif int(self.AgeEntry.get()) < 0:
            self.WarningLabel.configure(text = "You are too old") 
            self.AgeEntry.delete(0, END) 
            self.AgeEntry.focus() 
        elif int(self.AgeEntry.get()) < 7: 
            self.WarningLabel.configure(text = "You are too young")
            self.AgeEntry.delete(0, END) 
            self.AgeEntry.focus() 
            
        else:
            self.Welcome. grid_remove() 
            self.Questions.grid() 
            
    except ValueError: 
        self.WarningLabel.configure(text = "Please enter a number") 
        self.AgeEntry.delete(0, END) 
        self.AgeEntry.focus() 
