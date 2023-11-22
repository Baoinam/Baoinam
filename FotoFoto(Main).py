import customtkinter 
import tkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

root = customtkinter.CTk()
root.geometry('1000x600')
root.title('FotoFoto')
root.config(bg="gray")
options_fm = tk.Frame(root, background='white')


def switch(indicator_lb, page):
    for child in options_fm.winfo_children():
        if isinstance(child, ctk.Label):
            child['bg'] = 'SystemButtonFace'

    indicator_lb['bg'] = 'black'
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()

    page()
    

#Buttons of the project
Pictures_btn = ctk.Button(options_fm, text='Pictures', font=('Times New Roman', 13), bd=0, fg='Black', activebackground='#0097e8', command=lambda: switch(indicator_lb=Pictures_indicator_lb, page=Pictures_page))
Pictures_btn.place(x=0, y=0, width=125)
Pictures_indicator_lb = ctk.Label(options_fm)
Pictures_indicator_lb.place(x=0, y=30, width=125, height=2)



albums_btn = ctk.Button(options_fm, text='Albums', font=('Times New Roman', 13), bd=0, fg='Black', activebackground='#0097e8', command=lambda: switch(indicator_lb=albums_indicator_lb, page=albums_page))
albums_btn.place(x=130, y=0, width=125)
albums_indicator_lb = ctk.Label(options_fm)
albums_indicator_lb.place(x=130, y=30, width=125, height=2)



Favorites_btn = ctk.Button(options_fm, text='Favorites', font=('Times New Roman', 13), bd=0, fg='Black', activebackground='#0097e8', command=lambda: switch(indicator_lb=Favorites_indicator_lb, page=Favorites_page))
Favorites_btn.place(x=260, y=0, width=125)
Favorites_indicator_lb = ctk.Label(options_fm)
Favorites_indicator_lb.place(x=260, y=30, width=125, height=2)


Edit_btn = ctk.Button(options_fm, text='Edit', font=('Times New Roman', 13), bd=0, fg='Black', activebackground='#0097e8',command=lambda: switch(indicator_lb=Edit_indicator_lb ,page=Edit_page))
Edit_btn.place(x=390, y=0, width=125)
Edit_indicator_lb = ctk.Label(options_fm)
Edit_indicator_lb.place(x=390, y=30, width=125, height=2)






options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=516, height=32)


#Every page label
def Pictures_page():
    Pictures_page_fm = ctk.Frame(main_fm, bg="white")
    Pictures_page_lb = ctk.Label(Pictures_page_fm, text='Pictures', font=('Times New Roman', 13), fg='black')
    Pictures_page_fm.pack(fill=ctk.BOTH, expand=True)

def albums_page():
    albums_page_fm = ctk.Frame(main_fm, bg="white")
    albums_page_lb = ctk.Label(albums_page_fm, text='Albums', font=('Times New Roman', 13), fg='black')
    albums_page_lb.pack(pady=80)
    albums_page_fm.pack(fill=ctk.BOTH, expand=True)

   

def Favorites_page():
    Favorites_page_fm = ctk.Frame(main_fm, bg="white")
    Favorites_page_lb = ctk.Label(Favorites_page_fm, text='Favorites', font=('Times New Roman', 13), fg='black')
    Favorites_page_lb.pack(pady=80)
    Favorites_page_fm.pack(fill=ctk.BOTH, expand=True)
    
    


def Edit_page(): 
    Edit_page_fm = ctk.Frame(main_fm, bg="white")
    Edit_page_lb = ctk.Label(Edit_page_fm, text='Edit', font=('Times New Roman', 13), fg='black')
    Edit_page_lb.pack(pady=80)
    Edit_page_fm.pack(fill=ctk.BOTH, expand=True)
    
    
main_fm = ctk.Frame(root)
main_fm.pack(fill=ctk.BOTH, expand=True)

Pictures_page()
root.mainloop()
