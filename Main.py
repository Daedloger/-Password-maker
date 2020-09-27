import random as rd
from tkinter import *
import sqlite3 as sq

#just memory on sqlite3
with sq.connect('memory.db') as memory_on_sql:   #ther we make our database on users pc
    sql_memory_ = memory_on_sql.cursor()

    sql_memory_.execute('''CREATE TABLE IF NOT EXISTS memory_sql (
        password TEXT NOT NULL   
    )''') #internet will be text format!

    memory_on_sql.commit()

    #general programm!
    window = Tk()

    #themes changer!
    window.geometry("600x400")
    window.title("Password Maker ALPHA")
    window.configure(bg = "#ffffff")

    #button for theme!
    def clicked3():
        themes = ["Black", "White"]
        choice = rd.choice(themes)
        if choice == "Black":
            window.configure(bg = "#4d4d4d")
        if themes == "White":
            window.configure(bg = "#ffffff")
            
    theme = Button(window, text="Change theme", command=clicked3, background="#555",     # background of button
                                                        foreground="#ccc",     #COlor of text
                                                        padx="20",             # отступ от границ до содержимого по горизонтали
                                                        pady="8",              # отступ от границ до содержимого по вертикали
                                                        font="16"              # how high will bw text)))
                                                        )

    theme.grid(column = 5, row = 9)

    
    #Password things
    ALL = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", ".", "!", "-", "_", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    password = ""
    x = password
    
    #programm memory code
    memory = []
    
    #Input from user
    e = Entry(width = 50)
    
    #"Generate" button code
    def clicked():
        global password
        password = ""
        for i in range(8):
            password += password.join(rd.choice(ALL))
        memory.append(password)
        x = Label(window, text = password, font = ("Arial", 8))
        x.grid(column=5, row=6)
        x.configure(text=password)
    btn = Button(window, text="Generate", command=clicked, background="#555",     
                                                        foreground="#ccc",     
                                                        padx="20",             
                                                        pady="8",              
                                                        font="16"              
                                                        )
    btn.grid(column=5, row=5)
    
    #"Memory" button code
    name = 0
    memory_on_sql.execute(f"INSERT INTO memory_sql VALUES ('{password}', '{name}')")
    memory_on_sql.commit()

    def clicked1():
        global memory
        a = Label(window, text = memory_on_sql, font = ("Arial", 8))
        a.grid(column=5, row=8)
        a.configure(text=memory_on_sql) 
    memor = Button(window, text="Memory", command=clicked1, background="#555",     
                                                            foreground="#ccc",     
                                                            padx="20",             
                                                            pady="8",             
                                                            font="16"              
                                                            )
    memor.grid(column=5, row=7)

  

    window.mainloop()
    ''' Now I don't know how to show data in tkinter.
