from tkinter import Tk


# import tkinter
class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry('200x150 + 400 + 300')


root=Tk()
obj=Login(root)
root.mainloop()
