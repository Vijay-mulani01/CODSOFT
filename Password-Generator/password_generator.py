from tkinter import *
import tkinter.messagebox as tmsg
import random
import string

root=Tk()
root.geometry("450x600")
root.title("Password Generator")

def generate_password():
    
    try:
        length=int(length_value.get())
    except:
        tmsg.showerror("Error", "Please Enter Length")
        
    try:
        comp=int(complexity_value.get())
        char=""
        if comp>=1:
            char += string.ascii_letters
        if comp>=2:
            char += string.digits
        if comp>=3:
            char += string.punctuation
    except:
        tmsg.showerror("Error", "Please Enter Complexity")
    result=""
    result=''.join(random.choices(char, k=length))
    password=Entry(frame, textvariable=pass_value, font="arial 13 bold")
    password.config(state="disabled")
    password.grid(row=3, column=2)
    pass_value.set(result)

def reset():
    user_value.set("")
    complexity_value.set("")
    length_value.set("")
    pass_value.set("")

label=Label(root, text="Password Generator", fg="blue", font="arial 20 bold")
label.pack()

frame=Frame(root)
frame.pack(pady=50)
user_label=Label(frame, text="Enter Username : ", font="arial 12 bold", pady=20)
user_label.grid(row=0, column=1)
length_label=Label(frame, text="Enter Password Length : ", font="arial 12 bold", pady=20)
length_label.grid(row=1, column=1)
complexity_label=Label(frame, text="Complexity : ", font="arial 12 bold", pady=20)
complexity_label.grid(row=2, column=1)
pass_label=Label(frame, text="Generated Password : ", font="arial 12 bold", pady=20)
pass_label.grid(row=3, column=1)

user_value=StringVar()
length_value=StringVar()
complexity_value=StringVar()
pass_value=StringVar()

user=Entry(frame, textvariable=user_value, font="arial 12")
user.grid(row=0, column=2)
length=Entry(frame, textvariable=length_value, font="arial 12")
length.grid(row=1, column=2)
complexity=Entry(frame, textvariable=complexity_value, font="arial 12")
complexity.grid(row=2, column=2)


generator=Button(root, text="GENERATE PASSWORD",bg="#5f38e0",fg="white", font="arial 10 bold", command=generate_password)
generator.pack()

reset=Button(root, text="RESET",bg="#5f38e0",fg="white", font="arial 10 bold", command=reset)
reset.pack(pady=20)

root.mainloop()