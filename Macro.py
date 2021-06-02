import pydirectinput
import time
import random
from tkinter import *
value = bool
#py tinker
root = Tk()
root.title("Totally not sus")
app_width = 350
app_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
# input field
e = Entry(root,width=50)
def stop():
    global value
    value = False
    e.config(state='normal')
#spam input key
def loop():
        time.sleep(random.uniform(0, 2))
        pydirectinput.keyDown(e.get())
        pydirectinput.keyUp(e.get())
        if value == False:
            pass
        else:
            root.after(100,loop)
#check whether the is a input value
def start():
    if len(e.get()) == 0:
        text = Label(root,text="Input a key u want to loop")
        text.grid(row=2,column=1,columnspan=2,padx=20,pady=10)
        pass
    elif len(e.get()) > 1:
        text = Label(root,text="Only one key is allowed")
        text.grid(row=2,column=1,columnspan=2,padx=20,pady=10)
        pass
    else:
        e.config(state='disabled')
        loop()
    
#buttons
button1= Button(root,text="Start",padx=10,pady=10, command=start)
button2= Button(root,text="Stop",padx=10,pady=10, command=stop)
# grid style
e.grid(row=1,column=1,columnspan=2,pady=24,padx=20)
button1.grid(column=1,row = 3,padx=10,pady=10)
button2.grid(column=2,row = 3,padx=10,pady=10)

root.mainloop()

