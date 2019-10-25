from tkinter import *


class Window:
    def __init__(self, master):
        master.title("HeartRate and SPO2")
        master.geometry("1200x800")
        master.configure(bg="#0B0B0B")


class Components:
    def __init__(self, master):

        label = Label(master, text="Uzupełnij dane", fg='white', bg="#0B0B0B",
              font= ('Courier', 44), anchor='center')
        label.pack(pady=50)

        frame1= Frame(master, bg="#0B0B0B", width="300", height="200")
        frame1.pack(padx=50)

        frame2 = Frame(master, bg="#0B0B0B", width="300", height="200")
        frame2.pack(padx=50)

        frame3 = Frame(master, bg="#0B0B0B", width="300", height="200")
        frame3.pack(padx=50)

        label2 = Label(frame1, text="Imie", fg="white", font=('Courier', 35)
                       , bg="#0B0B0B", anchor='center')
        label2.pack()

        label3 = Label(frame2, text="Wiek", fg="white", font=('Courier', 35)
                       , bg="#0B0B0B", anchor='center')
        label3.pack()

        label4 = Label(frame3, text="Email", fg="white", font=('Courier', 35)
                       , bg="#0B0B0B", anchor='center')
        label4.pack()

        entry1=Entry(frame1, font=('Courier', 35))
        entry2=Entry(frame2, font=('Courier', 35))
        entry3=Entry(frame3, font=('Courier', 35))
        entry1.pack()
        entry2.pack()
        entry3.pack()


root = Tk()
Window(root)
Components(root)
root.mainloop()
