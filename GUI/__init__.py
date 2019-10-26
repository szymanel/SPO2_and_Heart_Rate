from tkinter import *


class Window:
    def __init__(self, master):
        master.title("HeartRate and SPO2")
        master.geometry("1200x800")
        master.configure(bg="#1C1C1C")

class Components:

    def __init__(self, master):

        self.label = Label(master, text="Uzupełnij dane", fg='white', bg="#1C1C1C",
              font = ('Courier', 44), anchor='center')
        self.label.pack(pady=50)

        self.frame1= Frame(master, bg="#1C1C1C", width="300", height="200")
        self.frame1.pack(padx=50)

        self.frame2 = Frame(master, bg="#1C1C1C", width="300", height="200")
        self.frame2.pack(padx=50)

        self.frame3 = Frame(master, bg="#1C1C1C", width="300", height="200")
        self.frame3.pack(padx=50)

        self.label2 = Label(self.frame1, text="Imie", fg="white", font=('Courier', 35)
                    , bg="#1C1C1C", anchor='center')
        self.label2.pack()

        self.label3 = Label(self.frame2, text="Wiek", fg="white", font=('Courier', 35)
                       , bg="#1C1C1C", anchor='center')
        self.label3.pack()

        self.label4 = Label(self.frame3, text="Email", fg="white", font=('Courier', 35)
                       , bg="#1C1C1C", anchor='center')
        self.label4.pack()

        self.entry1 = Entry(self.frame1, font=('Courier', 35))
        self.entry2 = Entry(self.frame2, font=('Courier', 35))
        self.entry3 = Entry(self.frame3, font=('Courier', 35))
        self.entry1.pack()
        self.entry2.pack()
        self.entry3.pack()

    def Create_Button (self, master):

        self.canvas = Canvas(master, bg="#1C1C1C", width="230", height="120")
        self.canvas.pack(pady=50)
        self.canvas.create_rectangle(0,120,230,0)
        self.canvas.bind("<Enter>",Events.enter_on_canvas)
        self.canvas.bind("<Leave>", Events.leave_on_canvas)
        self.canvas.create_text(115,60,fill="white",font=("Courier",35),
                        text="Pomiar")

class Events:
    def enter_on_canvas(event):
        C.canvas.configure(bg="#151515")
    def leave_on_canvas(event):
        C.canvas.configure(bg="#1C1C1C")


root = Tk()
E=Events
Window(root)
C=Components(root)
C.Create_Button(root)
root.mainloop()
