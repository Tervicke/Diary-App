import tkinter
from tkinter import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import ttk
import os 
from datetime import datetime
from datetime import timedelta  

#main_window settings //
main_window = tkinter.Tk()
main_window.geometry("1000x620")
main_window.resizable(False,False)
main_window.title('Diary')
#Editor Area 
Editor = tkinter.Text(main_window , height = 28 , width = 72 , fg='#121212' , bg='white' ,   padx='10' , pady='10' ,wrap=WORD)
Font_tuple = ("Sans Serif", 12, "normal")
Editor.configure(font = Font_tuple)

# calendar 
Cal = Calendar(main_window, selectmode = 'day' , foreground='#121212' ,  background="white" , bordercolor = 'white' , headersbackground = 'white' , headersforeground="#121212" , normalbackground='white' ,normalforeground='#121212' , weekendbackground='white' , weekendbackforeground='#121212' , othermonthforeground = '#121212' , othermonthbackground='white',othermonthweforeground='#121212' , othermonthwebackground='white' , selectbackground='blue' , showweeknumbers=False , showothermonthdays=False)

#today's date
today = datetime.today()

#Button click function 
def SelectButtonFunction(Event=None):
    Save_btn.place_forget()
    Editor.config(state='normal' , fg='#696969')
    file_name = Cal.get_date().replace('/','-')+".text"
    Editor.delete('1.0',END)
    if os.path.exists(file_name):
        with open(file_name) as Diary_File:
            Editor.insert('1.0',Diary_File.read())
    else:
        Editor.insert('1.0',"No Diary Entry found :(")

    Editor.config(state='disable' , fg='#696969')

Select_btn = tkinter.Button(main_window, text = ' select ',command=SelectButtonFunction, bg='white' , fg='#121212' , activeforeground="blue" ,activebackground='white')

def GenerateTodaysFileName():
    return str(today.day)+"-"+str(today.strftime("%m"))+"-"+str(today.strftime("%y"))+".text"

def EditTodaysButtonFunction(event=None):
    Save_btn.place(x=767,y=230)
    Editor.focus_set()
    Editor.config(state='normal' , fg='#121212')
    Cal.selection_set(today) 
    def GenerateTodaysFormattedHeader():
        if today.day == 1:
            formatted_string = "* "+str(today.day)+"st "
        elif today.day == 2 or today.day == 22:
            formatted_string = "* "+str(today.day)+"nd "
        elif today.day == 3 or today.day == 23:
            formatted_string = "* "+str(today.day)+"rd "
        else: 
            formatted_string = "* "+str(today.day)+"th "
        return  formatted_string + str(today.strftime("%B"))+" "+str(today.strftime("%Y"))+",\n* "+str(today.strftime('%A'))

    Editor.delete("1.0",END)
    if os.path.exists(GenerateTodaysFileName()):
        #with open(GenerateTodaysFileName()) as Todays_File:
        Todays_File = open(GenerateTodaysFileName() , 'r')
        Editor.insert("1.0",Todays_File.read().rstrip())
    else:
        Editor.insert("1.0",GenerateTodaysFormattedHeader())

EditTodays_btn = tkinter.Button(main_window, text = 'edit today\'s',command=EditTodaysButtonFunction, bg='white' , fg='#121212' , activeforeground="blue" ,activebackground='white')

def SaveButtonFunction(event=None):
    Editor.config(state='disable' , fg='#696969')
    Todays_File = open(GenerateTodaysFileName() , 'w')
    Todays_File.write(Editor.get("1.0",END))
    Save_btn.place_forget()

Save_btn = tkinter.Button(main_window, text = 'save',command=SaveButtonFunction, bg='white' , fg='#121212' , activeforeground="blue" ,activebackground='white')

def NextButtonFunction(event=None):
    if not Save_btn.winfo_ismapped():
        Cal.selection_set(Cal.selection_get() + timedelta(1))
        SelectButtonFunction()

Next_btn= tkinter.Button(main_window, text = '>',command=NextButtonFunction, bg='white' , fg='#121212' , activeforeground="blue" ,activebackground='white')

def BackButtonFunction(event=None):
    if not Save_btn.winfo_ismapped():
        Cal.selection_set(Cal.selection_get() + timedelta(-1))
        SelectButtonFunction()

Back_btn= tkinter.Button(main_window, text = '<',command=BackButtonFunction, bg='white' , fg='#121212' , activeforeground="blue" ,activebackground='white')

Editor.bind("<Control-Key-s>",SaveButtonFunction)
Editor.bind("<Left>",BackButtonFunction)
Editor.bind("<Right>",NextButtonFunction)
Editor.bind("<Control-Key-e>",EditTodaysButtonFunction)

#adding everything onto the main_window
Editor.place(x=10,y=40)
Cal.place(x=767,y=44)
Select_btn.place(x=767 , y = 197)
EditTodays_btn.place(x=845 , y=197)

Next_btn.place(x=715,y=5)
Back_btn.place(x=675,y=5)
#displaying todays diary by deafult 
EditTodaysButtonFunction()

#display the main_window
main_window.mainloop()
