from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("900x500")
root.minsize(900,500)
root.title("To-Do List")

def add():
    value=entry.get()
    if value:
        lbx.insert(END,value)
        entry.delete(0, END)
    else:
        tmsg.showwarning("Error","Enter some task first")
    
def update():
    try:
        index=lbx.curselection()
        final_val=entry.get()
        if final_val:
            lbx.delete(index)
            lbx.insert(index, final_val)
            entry.delete(0, END)
        else:
            tmsg.showerror("Error", "First enter the updated Task")
    except:
        tmsg.showwarning("warning", "Please select a task")

def delete():
    index=lbx.curselection()
    if index:
        lbx.delete(index)
    else:
        tmsg.showwarning("warning", "Please select a task to delete")

label = Label(root, text="Add Items:", font="arial 15 bold", pady=15,padx = 15,borderwidth=10,anchor="w", justify="left",width=50)
label.pack()

entry_val=StringVar
entry=Entry(root, textvariable=entry_val, font="arial 15 bold", width=40, bg="#eff0e9")
entry.pack(padx=5, pady=5)

add_button=Button(root, text="Add",font="arial 10 bold", bg="#2b2e2c", fg="white", padx=20, command=add)
add_button.pack(pady=15)

scrollbar=Scrollbar(root)
scrollbar.pack(side="right", fill="y")

lbx=Listbox(root,width=80, font="arial 15 bold", yscrollcommand=scrollbar.set, bg="#eff0e9", relief=SUNKEN, fg="#141063")
scrollbar.config(command=lbx.yview)
lbx.pack(padx=25)


frame = Frame(root)
frame.pack(pady=15)
update_button=Button(frame, text="Update",font="arial 10 bold", bg="#2b2e2c", fg="white", padx=20, command=update)
update_button.grid(row=1, column=1, padx=15)

delete_button=Button(frame, text="Delete",font="arial 10 bold", bg="#2b2e2c", fg="white", padx=20, command=delete)
delete_button.grid(row=1, column=2)

root.mainloop()