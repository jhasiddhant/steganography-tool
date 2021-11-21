# Import libraries
from tkinter import *           # Import Tkinter
from Hide import hide           # Import Hide.py
from Unhide import unhide       # Import Unhide.py

# GUI for hiding message in image
def hide_message():

    def get_data():
        src = textbox1.get()
        message = textbox2.get()
        dest = textbox3.get()
        mesg = hide(src, message, dest)
        status = Label(hide_window, text= mesg, font=('Arial Bold', 20),fg='green')
        status.place(x=300, y=490)

    window.destroy()
    hide_window = Tk()
    hide_window.geometry("1000x600")

    img = PhotoImage(file="background.png")
    label = Label(hide_window, image=img)
    label.place(x=0, y=0)

    title2 = Label(hide_window, text='Hide Message', font=('Arial Italic', 40), bg=None)
    title2.place(x=360 ,y=50)

    add_image = Label(hide_window,text='Add source image',font=('Arial Bold', 20))
    add_image.place(x=200,y= 200)

    textbox1 = Entry(hide_window, font=('Arial Bold', 20), textvariable= StringVar(),width=15)
    textbox1.place(x=600, y=200)

    add_message = Label(hide_window, text='Enter message to hide', font=('Arial Bold', 20))
    add_message.place(x=200, y=280)

    textbox2 = Entry(hide_window, font=('Arial Bold', 20),textvariable= StringVar(),width=15)
    textbox2.place(x=600, y=280)

    destination = Label(hide_window, text='Enter destination image', font=('Arial Bold', 20))
    destination.place(x=200, y=360)

    textbox3 = Entry(hide_window, font=('Arial Bold', 20), textvariable=StringVar(), width=15)
    textbox3.place(x=600, y=360)

    hide_button = Button(hide_window, text='Hide', height=1, width=10, bg='#554cfe', fg='White',
                         font=('Arial Bold', 20), command=get_data)
    hide_button.place(x=400, y=430)

    hide_window.mainloop()


# GUI for Revealing message in image
def unhide_message():

    def get_input():
        src = textbox1.get()
        print(src)
        final_message = unhide(src)
        disp_message = Label(unhide_window, text= 'Hidden Message: '+ final_message, font=('Arial Bold', 20),fg='green')
        disp_message.place(x=320, y=360)


    window.destroy()

    unhide_window = Tk()
    unhide_window.geometry("1000x600")

    img = PhotoImage(file="background.png")
    label = Label(unhide_window, image=img)
    label.place(x=0, y=0)

    title3 = Label(unhide_window, text='Unhide Message', font=('Arial Italic', 40))
    title3.place(x=360, y=50)

    add_image = Label(unhide_window, text='Add source image', font=('Arial Bold', 20))
    add_image.place(x=200, y=200)

    textbox1 = Entry(unhide_window, font=('Arial Bold', 20), textvariable=StringVar() ,width=15)
    textbox1.place(x=600, y=200)

    unhide_button = Button(unhide_window, text='Unhide', height=1, width=10, bg='#554cfe', fg='White',
                           font=('Arial Bold', 20),command= get_input)
    unhide_button.place(x=400, y=280)


    unhide_window.mainloop()


if __name__=='__main__':

    window = Tk()
    window.geometry("1000x600")

    img = PhotoImage(file="background.png")
    label = Label(window,image=img)
    label.place(x=0, y=0)

    title = Label(window,text='Steganography',font=('Arial Italic', 40))
    title.place(x=360, y=50)

    button1 = Button(window, text='Hide Message', height=2, width=15, bg='#554cfe', fg='White',font=('Arial Bold', 20),
                     command=hide_message)
    button1.place(x=400,y= 150)

    button2 = Button(window, text='Unhide Message', height=2, width=15, bg='#554cfe', fg='White', font=('Arial Bold', 20),
                     command= unhide_message)
    button2.place(x=400, y=280)


    window.mainloop()