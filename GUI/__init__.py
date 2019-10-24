from tkinter import*


class Window:
    def __init__(self,master):
        master.title("HeartRate and SPO2")
        master.geometry("1200x800")
        self.L = Label(text="Uzupełnij Dane", fg='white', bg='#0B0B0B',anchor='n',width=200, height=100,font=('Courier',44))
        self.L.pack()


root = Tk()
Window(root)
root.mainloop()