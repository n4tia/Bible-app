import os, csv, bibleapi as bibleapi
from tkinter import *
from tkinter import messagebox as mb
from tkinter.simpledialog import askinteger
import tkinter as tk 

root=Tk()
root.geometry('+0+0')

def getcontent(x):
    global data
    global new_win
    global chapter
    chapter=x
    header=list(['BookID','OsisID','BookName','TotalChapters','Volume','Chapters','Verses','Avg Verse'])
    '''try:
        new_win.destroy()
        new_win.update()
    except:
        pass'''
    new_win=Toplevel()    
    new_win.geometry('+650+0')
    new_win.title(data[int(chapter)][2])
    col=-1
    for i,items in enumerate(data[int(chapter)]):
        if i==0 or i==2 or i==3:
            col+=1
            
            Label(new_win,width=20,bg='#C4CAD0', text=header[i]).grid(column=col, row=0,padx=10,pady=5)
            
            Label(new_win,width=20,bg='#C4CAD0', text=header[i]).grid(column=col, row=0,padx=10,pady=5)
            
            if i!=3:
                Label(new_win,width=20, text=items,bg='#E0E1E8').grid(column=col, row=1,padx=10,pady=5)
            else:
                my_list=list()
                end=int(data[int(chapter)][3])+1
                for i in range(1,end):
                    my_list.append(f'chapter {i}')
                my_var=IntVar(new_win,'chapter: ')
                opt=OptionMenu(new_win,my_var, *my_list, command=getverse)
                opt.grid(row=1,column=2)
def getverse(x):
    global data
    global chapter
    global new_win,my_verse
    chapter_number=x.split()[1]
    verse=askinteger('enter verse', 'verse number')
    my_verse=bibleapi.api_get_bible(data[chapter][2],chapter_number,verse)
    my_verse=list(my_verse.values())
    new_win.geometry('+650+0')
    Label(new_win, text=f'{my_verse[1]} chapter {my_verse[2]} verse {my_verse[3]}').grid(column=0, row=2, columnspan=3)
    Label(new_win, text=f'{my_verse[4]}').grid(column=0, row=3, columnspan=3)
    canvas = tk.Canvas(new_win,  
                   width = 200,  
                   height = 200) 
  
    
    save_btn = Button(new_win, 
            text ='Save', 
            command = option_to_save).grid(column=0, row=4, columnspan=3)
    canvas.create_window(100, 100,  
                     window = save_btn) 
    
    
def option_to_save():
    global data,chapter,new_win,my_verse
    save_qeust=mb.askquestion('Do you want to save information to file?', 'Do you want to save information to file?')
    if save_qeust == 'yes' :
        with open('saved_information.txt', 'w') as f:
            for line in my_verse:
                f.write("%s\n" % line)
        mb.showinfo('Save','Saved.')
    else :
        mb.showinfo('Return', 'Returning to main application')
     
def display_text():
   global str,data,chapter,new_win,my_verse
   str= Entry.get()
   Label.configure(text=str)
 
root.config(bg='#FCF7FF')

data=[]


my_path=os.path.dirname(os.path.abspath(__file__))
my_path=os.path.join(my_path, "bible.csv")


with open (my_path, 'r') as file:
    reader=csv.reader(file)
    for i, row in enumerate(reader):
        if i !=0:
            data.append(row)
           

col=0
ro=0
btn_list=[]
for i,items in enumerate(data):
    if i % 4 ==0:
        col=5
        ro +=1
    #print(items[2])
    col +=1
    btn_list.append(Button(root, width=20,bg='#E0E1E8',text=items[2],command=lambda x=i:getcontent(x)))
    
    btn_list[i].grid(column=col, row=ro)  


root.mainloop()