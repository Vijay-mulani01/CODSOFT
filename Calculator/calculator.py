from tkinter import *
import math

root=Tk()
root.geometry("290x433")
root.minsize(290,433)
root.maxsize(500,500)
root.title("Calculator")
root.wm_iconbitmap("./Calculator/calculator-icon.ico")

def screen_data(event):
   val = event.widget.cget("text")
   if val=="=":
      if("√" in screen_value.get()):
         scr_value=int(str(screen_value.get()).replace('√', ''))
         value=math.sqrt(scr_value)

      elif("log" in screen_value.get()):
         scr_value=int(str(screen_value.get()).replace('log', ''))
         value=math.log(scr_value)

      elif screen_value.get().isdigit():
         value=int(screen_value.get())
      
      else:
         value=eval(screen.get())
      screen_value.set(value)
      screen.update()
   elif val=="C":
      screen_value.set("")
      screen.update()
   else:
      screen_value.set(screen_value.get() + val)
      screen.update()


frame1=Frame(root, bg="gray",padx=5, pady=15)
frame1.pack(fill="x")

screen_value=StringVar()
screen_value.set("")
screen=Entry(frame1, textvariable=screen_value, fg="white", bg="black", font="arial 26")
screen.pack(fill="x", side="bottom")

frame2=Frame(root, bg="black", padx=5, pady=5)
frame2.pack()

row = 1
col = 1
colcount = 5
btn_list=['C','%','/','+','9','8','7','*','6','5','4','-','3','2','1','=','√','0','.','log']
for number in btn_list:
    txt=str(number)
    btn_name="btn"+ txt
    btn_name=Button(frame2, text=txt,bg="black",fg="orange", font="arial 26",height=1, width=3, command=screen)
    btn_name.grid(row = row, column = col)
    btn_name.bind('<Button-1>',screen_data)
    col += 1
    if col == colcount:
        col = 1
        row += 1

root.mainloop()