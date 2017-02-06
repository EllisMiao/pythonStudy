from tkinter import * #引入模块
def resize(ev=None):
    label.config(font='Helvetic -%d bold'% scale.get())
top=tkinter.Tk()
label=Label(top,text="This is a Test",font="Helvetia -12 bold")
label.pack(fill=Y,expand=1)
scale=Scale(top,from_=10,to=40,orient=VERTICAL,command=resize)
scale.set=(12)
scale.pack(fill=x,expand=1)
quit=Button(top,text="QUIT",command=top.quit,activeforeground="white",activebackground="red")
quit.pack()
