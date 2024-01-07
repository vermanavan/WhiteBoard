from tkinter import *
import customtkinter as ctk
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

#window attributes using tkinter
root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg='#f2f3f5')
root.resizable(False, False)


#################Definations##################
current_x=0
current_y=0
color="black"

def locate_xy(work):

    global current_x,current_y
    current_x=work.x
    current_y=work.y

def addline(work):
    global current_x,current_y

    canvas.create_line((current_x,current_y,work.x,work.y),
                       width=get_current_value(),
                       fill=color,capstyle=ROUND,
                        smooth=True)
    current_x,current_y=work.x,work.y

def show_color(new_color):
    global color
    color=new_color

def new_canvas():
    canvas.delete('all')
    display_pallet()


def insertImage():
    global filename
    global f_image
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select image",
                                        filetype=(("PNG file","*.png"),("ALL files","new.txt")))

    f_image=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(180,50,image=f_image)
    root.bind("<B3-Motion>",my_callback)

def my_callback(event):
    global f_image
    f_image=tk.PhotoImage(file=filename)
    my_img=canvas.create_image(event.x,event.y,image=f_image)



#####################icon###########################

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

#############################sideBar#####################

color_box= PhotoImage(file="color section.png")
Label(root,image=color_box,bg='#f2f3f5').place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg='#f2f3f5',command=new_canvas).place(x=30,y=400)

importimage=PhotoImage(file="addimage.png")
Button(root,image=importimage,bg='#f2f3f5',command=insertImage).place(x=30,y=450)

colors=Canvas(root,bg='#fff',width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_pallet():
    id=colors.create_rectangle(10,10,30,30,fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('black'))

    id=colors.create_rectangle(10,40,30,60,fill='gray')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('gray'))

    id=colors.create_rectangle(10,70,30,90,fill='brown4')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('brown4'))

    id=colors.create_rectangle(10,100,30,120,fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('red'))

    id=colors.create_rectangle(10,130,30,150,fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('orange'))

    id=colors.create_rectangle(10,160,30,180,fill='yellow')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('yellow'))

    id=colors.create_rectangle(10,190,30,210,fill='green')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('green'))

    id=colors.create_rectangle(10,220,30,240,fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('blue'))

    id=colors.create_rectangle(10,250,30,270,fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x:show_color('purple'))

display_pallet()

####################main_screen###################

canvas=Canvas(root,width=930,height=500,background='white',cursor='hand2')
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addline)

######################slider######################

current_value=ctk.DoubleVar()
def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=current_value.get())

value_label=ctk.CTkLabel(root,text=get_current_value)
value_label.place(x=27,y=550)

slider = ctk.CTkSlider(master=root,from_=0,to=100,
                                 width=100,
                                 height=16,
                                 border_width=7,
                                 command=slider_changed,
                                 variable=current_value)
slider.place(x=50, y=530, anchor=tk.CENTER)     
                               
                   

root.mainloop()