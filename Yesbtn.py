from tkinter import *
from tkinter import messagebox
import random
def no():
    messagebox.showinfo(' ', 'Thanks bro')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text="Are you stupid ?", font='Azrial 20 bold', bg='white').pack()
btnYes = Button(root, text='No', font='Azrial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Yes', font='azrial 20 bold', command=no).place(x=350, y=100)

root.mainloop()