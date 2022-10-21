#Importing Modules
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
from functools import partial
import os
import shutil
import collections

#Setting up the Size, Title, Icon and other properties of the Window
root = Tk()
root.geometry("428x340")
root.title("Copy Kat")
root.resizable(0,0)

#About us ---> Menu Bar Calls
def about():
    messagebox.showinfo("About", "AI group project (Copy Kat) by Abhishek, Mehran, Rishu, Saurabh and Vishal.")


#Function to clear textfield when it is clicked for the first time
count=1
def handle_click(event):
    global count
    if(select_folder.get() == "Select a folder"):
        select_folder.delete(0,END)

#key_press handling
def key_handling(self):
    if(select_folder.get()!="Select a folder" or select_folder.get()!=""):
        add_button['state'] = 'normal'
    else:
        add_button['state'] = 'disabled'

#Browse Function
def browse():
    global select_folder
    select_folder.delete(0,END)
    address = filedialog.askdirectory()
    select_folder.insert(0,address)
    if select_folder.get() == "" or select_folder.get() == "Select a folder":
        address = "Select a folder"
        select_folder.insert(0, address)
        add_button['state'] = 'disabled'
    else:
        add_button['state'] = 'normal'

#Adding ComboBox
# n = IntVar()
# def add_combo():
#     print(n)
#     dp_menu = Combobox(column_main, textvariable=n, width=23,height=0,font=('Arial', 6),state='disabled')
#     # dp_menu.grid(row=1, column=1)
#
#     dp_menu.pack()
#     dp_menu['values'] = ('Temporary', 'Permanent')
#     dp_menu.current(0)


#Handing Add Button Event
lists=[]
click=0

def add():
    global click
    isdir = os.path.isdir(select_folder.get())
    print("count is: " + str(click))
    if(isdir == 1):
        lists.append(select_folder.get())
        sets = set(lists)
        temp_list = list(sets)
        if collections.Counter(sets) == collections.Counter(lists):
            print("same hai bhaiya")
            run_button['state'] = 'normal'
            print(lists)
            click+=1
            print("count is: " + str(click))
            list_boxes(lists[click-1])
        elif len(lists) > 1:
            print("Not same bhaiya")
            print(lists)
            messagebox.showinfo("Warning!", "Folder already exist in the list.")
            lists.pop()
            print(lists)
    else:
        messagebox.showwarning(title="Invalid Folder", message="Folder doesn't exist.")
    print(isdir)



#creating list box
def list_boxes(index):
    global click
    print("I am called bitch")
    # list_box = Listbox(column1, width=40, height=1,bd=0,font=('Arial', 10),borderwidth=0, highlightthickness=0)
    list_box.insert(END,index)
    # list_box.grid(row=1,column=0,sticky=N)
    list_box.bind("<Button-1>", folder_selected)
    text = list_box.get(0, "end")
    print("This is " + str(text))
    list_box.pack(side="top")
    # add_combo()


#Folder Selected ACtions
def folder_selected(self):
    remove_selected['state'] = 'normal'

#Create the Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Creating file menu
file_menu = Menu(my_menu, tearoff=False, activeborderwidth=1.6, bd=3,font=("Verdana, 9"))
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Home")
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

#Creating Help Menu
help_menu = Menu(my_menu, tearoff=False, activeborderwidth=1.6, bd=3,font=("Verdana, 9"))
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

#User Input Area - Topmost frame
# input_frame = LabelFrame(root, text="Select a folder:", padx=5, pady=5, bd=2)
# input_frame.grid(row=0, column=0, padx=10, pady=7,sticky=E+W)

input_frame = Frame(root)
input_frame.grid(row=0, column=0, padx=17, pady=7, sticky=E+W)

select_folder = Entry(input_frame,width=42,fg="brown")
select_folder.insert(0,"Select a folder")
select_folder.bind("<Button-1>", handle_click)
select_folder.bind("<Key>", key_handling)
select_folder.grid(row=0, column=0)

browse_button = Button(input_frame, text="Browse", command=browse)
browse_button.grid(row=0, column=1, padx=10)

add_button = Button(input_frame, text="Add to List", state= DISABLED, command=add)
add_button.grid(row=0, column=2)

#Main Area
main_frame = LabelFrame(root, bg="white")
main_frame.grid(row=1, column=0, padx=9,sticky=N+S+E+W)
root.grid_rowconfigure(1,weight=1)


# column1  = LabelFrame(main_frame,bd=0,bg="white")
# column1.grid(row=0, column=0)
#
# column2  = LabelFrame(main_frame,bd=0)
# column2.grid(row=0, column=1)

list_box = Listbox(main_frame, width=56, height=len(lists),bd=0,font=('Arial', 10),borderwidth=0, highlightthickness=0)


# label = Label(column2, text="Label2")
# label.grid(row=0, column=1)

# column_main = LabelFrame(main_frame, bd=0,bg="white")
# column_main.pack()
# label = Label(column_main,text="main")
# label.grid(row=0,column=0)

# dp_menu = Combobox(column_main, textvariable=n, width=23,height=len(lists),font=('Arial', 6),state='disabled')


location = Label(main_frame, text="Location", relief= RAISED)
# location.grid(row=0, column=0, ipadx=111, ipady=2)
# location.grid(row=0,column=0,ipadx=111, ipady=2)
location.pack(fill='x',ipadx=120, ipady=2)

# state = Label(column_main, text="State", relief= RAISED)
# state.grid(row=0, column=1, ipadx=50, ipady=2)
# state.pack(fill='x', ipadx=42, ipady=2)

#Working with list of folder added for action
# list_box = Listbox(column1, width=40, height=len(lists),bd=0,font=('Arial', 10),borderwidth=0, highlightthickness=0)
# for items in lists:
#     list_box.insert(END,items)
# # list_box.grid(row=1,column=0,sticky=N)
# list_box.pack()


#Creating a dropdown menu in the Status Section
# for i in range(0,len(lists)):
#     clicked = IntVar()
#     dp_menu = Combobox(main_frame, textvariable=lists)
#     dp_menu.grid(row=i+1,column=1)

# n = StringVar()

# dp_menu = Combobox(column_main, textvariable=n, width=23,height=0,font=('Arial', 6),state='disabled')
# # dp_menu.grid(row=1, column=1)
# dp_menu.pack()

# dp_menu1 = Combobox(column_main, textvariable=n, width=23,height=0,font=('Arial', 6))
# # dp_menu1.grid(row=2, column=1)
# dp_menu1.pack()
#
# dp_menu2 = Combobox(column_main, textvariable=n, width=23,height=0,font=('Arial', 6))
# # dp_menu2.grid(row=3, column=1)
# dp_menu2.pack()

# dp_menu['values'] = ('Temporary', 'Permanent')
# dp_menu.current(0)



#Bottom Area --> Status Bar, Run and Remove Selected Button
botoom_frame = Frame(root, padx=1, pady=5)
botoom_frame.grid(row=2,column=0, sticky=E+W)

def makeDir(list2):
    for item in list2:
        path1 = item + "/Copy Kat"
        path = str(path1)
        exist = os.path.exists(path)
        print("exist is " + str(exist))
        if exist== FALSE:
            print("OO beta jee: " + str(path))
            try:
                os.mkdir(path)
                print("DIR WORKED")
                folders = ["Documents", "Music", "Programs", "Videos", "Compressed", "Pictures", "Others" ]
                for folder in folders:
                    try:
                        os.mkdir(path+"/"+folder)
                        print("Beta jee 2")
                    except:
                        pass
            except:
                pass

def move_files(lists):
    try:
        for item in lists:
            path = item + '/Copy Kat/'
            for file in os.listdir(item):
                item_loc = item+'/'+file
                if (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".bmp") or file.endswith(".tiff") or file.endswith(".psd") or file.endswith(".gif")):
                    shutil.move(item_loc , path+"Pictures/"+file)
                elif (file.endswith(".mp4") or file.endswith(".ts") or file.endswith(".3gp") or file.endswith(".mpeg") or file.endswith(".mov") or file.endswith(".avi") or file.endswith(".flv") or file.endswith(".mkv") or file.endswith(".webm")):
                     shutil.move(item_loc, path+"Videos/"+file)
                elif (file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".pptx") or file.endswith(".txt") or file.endswith(".csv")):
                    shutil.move(item_loc, path+"Documents/"+file)
                elif (file.endswith(".rar") or file.endswith(".zip") or file.endswith(".tar") or file.endswith(".7z") or file.endswith(".iso")):
                    shutil.move(item_loc, path+"Compressed/"+file)
                elif (file.endswith(".mp3") or file.endswith(".3gpp") or file.endswith(".wav") or file.endswith(".m4a") or file.endswith(".wma") or file.endswith(".aac") or file.endswith(".flac") ):
                    shutil.move(item_loc, path+"Music/"+file)
                elif (file.endswith(".exe") or file.endswith(".ini") or file.endswith(".java")):
                    shutil.move(item_loc, path+"Programs/"+file)
                elif (file.endswith(".*")):
                    shutil.move(item_loc,path+"Others/"+file)
    except:
        messagebox.showwarning("Error","Something went wrong.\n Solution: If Copy Kat folder already exist, delete that.")
def main_Action(list1):
    print("Main Actin in ACtion")
    makeDir(list1)
    move_files(list1)
    messagebox.showinfo("Success!", "Files moved Successfully.\n Schrodinger's Cat Rocks..")


run_button = Button(botoom_frame, text="Run",state="disabled", command=partial(main_Action, lists))
run_button.pack(side=RIGHT,padx=10,ipadx=20)
# run_button.grid(row=0, column=1, sticky=W, padx=10,ipadx=15)

def remove():
    global click
    selection = list_box.curselection()
    if(selection):
        list_box.delete(ANCHOR)
        print("I am ANCHOR:" + list_box.get(ANCHOR))
        lists.pop()
        click-=1
        selection = list_box.curselection()
        if(click==0):
            remove_selected['state'] = 'disabled'
            run_button['state'] = 'disabled'
        if(selection):
            pass
        else:
            remove_selected['state'] = 'disabled'
        print("count is: " + str(click))
    else:
        messagebox.showwarning("Warning","Nothing selected..")



remove_selected = Button(botoom_frame, text="Remove Selected", state="disabled", command=remove)
remove_selected.pack(side=RIGHT)
# remove_selected.place(row=0, column=0, sticky=W)

home_button = Button(botoom_frame, text="Home")
home_button.pack(side=LEFT, padx=10, ipadx=20)

root.mainloop()