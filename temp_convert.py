from tkinter import *
import tkinter as tk

root= tk.Tk()
root.title("Temperature converter")

label = Label(root,text="",font= ("helvetica", 20))
label.grid(row="2", column="0")

lab_display = Label(root, text="",font=("arial",15))
lab_display.grid(row="1", column="0")
      
def tempc():
    lab_display.config(text="celsius to farenheit")   
    
def tempf():
    lab_display.config(text="farenheit to celsius")
    

def results():
    selectchoice= choice.get()
    if (selectchoice==1):
        inp= inputt.get("1.0",END)
        inp= float(inp)
        farenheit = inp * 1.8  + 32
        label.config(text= str(farenheit) + " degree farenheit", fg="red")
        
    elif (selectchoice==2):
        ino = inputt.get("1.0", END)
        ino= float(ino)
        celsius = (ino- 32)*(5/9)
        label.config(text= str(celsius)+ " degree celsius", fg= "blue")
        


inputt = Text(root, bg= "light blue", height=2, width=25)
inputt.grid(row="1", column="1")

but_check = Button(root,text="check", fg="yellow", bg="blue", command=results)
but_check.grid(row="1", column="2")

choice= tk.IntVar()
choice1= Radiobutton(root, text=("celsius"),variable= choice, value= 1,command=tempc).grid(row="0", column="0")
choice2= Radiobutton(root, text=("farenheit"),variable = choice, value = 2,command=tempf).grid(row="0", column="1")

root.mainloop()