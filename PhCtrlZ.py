from tkinter import *
from tkinter import messagebox
import webbrowser


def btnlogin_click():
	user= tbUser.get()
	mystr = str(user)
	url=mystr.replace("www", "mbasic")
	runprf=webbrowser.open_new_tab(url)
def cac_click():
	messagebox.showinfo("Url","Nhập link ở dưới")
frmlogin=Tk()
frmlogin.title("Đăng nhập")
frmlogin.geometry("400x280")
lb1= Label(frmlogin, text="Adminstrator login sever", font=("Time New Romen",18),fg="red")#fg=chọn màu
lb1.pack()
lb2= Button(frmlogin, text="nhập link ở dưới:",font=("Arial",12),fg="red",command=cac_click)
lb2.pack()
tbUser=Entry(frmlogin,width=30,font=("consolas",12))
tbUser.pack()
btnlogin=Button(frmlogin,text="Login",font=("san-serif",16,"bold"), fg="white",bg="red",command=btnlogin_click)
btnlogin.pack()
frmlogin.mainloop()