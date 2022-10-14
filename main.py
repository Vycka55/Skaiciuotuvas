from tkinter import *
from tkinter import scrolledtext


langas=Tk()

# Parent widget for the buttons


tekst = Entry()
tekst.grid(row=0, column=0)

buttons_frame = Frame(langas)
buttons_frame.grid(row=1, column=0, sticky=W+E) 


btn_7 = Button(buttons_frame, text='7')
btn_7.grid(row=1, column=0, padx=(0), pady=0)

btn_8 = Button(buttons_frame, text='8')
btn_8.grid(row=1, column=1, padx=(0), pady=0)

btn_9 = Button(buttons_frame, text='9')
btn_9.grid(row=1, column=2, padx=(0), pady=0)

btn_x = Button(buttons_frame, text='X')
btn_x.grid(row=1, column=3, padx=(0), pady=0)

btn_4 = Button(buttons_frame, text='4')
btn_4.grid(row=2, column=0, padx=(0), pady=0)

btn_5 = Button(buttons_frame, text='5')
btn_5.grid(row=2, column=1, padx=(0), pady=0)

btn_6 = Button(buttons_frame, text='6')
btn_6.grid(row=2, column=2, padx=(0), pady=0)

btn_min = Button(buttons_frame, text='-')
btn_min.grid(row=2, column=3, padx=(1), pady=1)

btn_1 = Button(buttons_frame, text='1')
btn_1.grid(row=3, column=0, padx=(1), pady=1)

btn_2 = Button(buttons_frame, text='2')
btn_2.grid(row=3, column=1, padx=(1), pady=1)

btn_3 = Button(buttons_frame, text='3')
btn_3.grid(row=3, column=2, padx=(1), pady=1)

btn_plus = Button(buttons_frame, text='+')
btn_plus.grid(row=3, column=3, padx=(1), pady=1)

btn_plusminus = Button(buttons_frame, text='+/-')
btn_plusminus.grid(row=4, column=0, padx=(1), pady=1)

btn_0 = Button(buttons_frame, text='0')
btn_0.grid(row=4, column=1, padx=(1), pady=1)

btn_kab = Button(buttons_frame, text=',')
btn_kab.grid(row=4, column=2, padx=(1), pady=1)

btn_kab = Button(buttons_frame, text='=')
btn_kab.grid(row=4, column=3, padx=(1), pady=1)


mainloop()