import customtkinter 
import tkinter as ctk
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

app = customtkinter.CTk()
app.geometry("400x300")


root = customtkinter.CTk()
root.geometry('720x720')
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
home_btn = ctk.Button(options_fm, text='Pictures', font=('Times New Roman', 13), bd=0, fg='Black', activebackground='#0097e8', command=lambda: switch(indicator_lb=home_indicator_lb, page=home_page))
home_btn.place(x=0, y=0, width=125)
home_indicator_lb = ctk.Label(options_fm)
home_indicator_lb.place(x=0, y=30, width=125, height=2)


frame = customtkinter.CTkFrame(master=app,corner_radius=20)
frame.pack(pady=20, padx=20, fill="both", expand=True)

button_1 = ctk.Button(master=frame,text="Add Photos",
                      corner_radius=8,
                      width=200,
                      height=30,
                      font=("Arial, 20)"),
                      border_spacing=10)
button_1.pack(padx=20, pady=20)

        


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
def home_page():
    home_page_fm = ctk.Frame(main_fm, bg="black")
    home_page_lb = ctk.Label(home_page_fm, text='Pictures', font=('Times New Roman', 13), fg='black')
    home_page_fm.pack(fill=ctk.BOTH, expand=True)

def albums_page():
    left_frame = ctk.Frame(root, width=200, height=600, bg="white")
    left_frame.pack(side="left", fill="y")
    filter_label = ctk.Label(left_frame, text="Select Filter", bg="white")
    filter_label.pack()
    albums_page_fm = ctk.Frame(main_fm, bg="black")
    albums_page_lb = ctk.Label(albums_page_fm, text='Albums', font=('Times New Roman', 13), fg='black')
    albums_page_lb.pack(pady=80)
    albums_page_fm.pack(fill=ctk.BOTH, expand=True)

    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="Yuki.png")
    image = Image.open(file_path)   
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

def Favorites_page():
    Favorites_page_fm = ctk.Frame(main_fm, bg="black")
    Favorites_page_lb = ctk.Label(Favorites_page_fm, text='Favorites', font=('Times New Roman', 13), fg='black')
    Favorites_page_lb.pack(pady=80)
    Favorites_page_fm.pack(fill=ctk.BOTH, expand=True)
    
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="Yuki.png")
    image = Image.open(file_path)   
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    canvas.pack()


canvas = ctk.Canvas(root, width=1000, height=1000)




def Edit_page():
    
    Edit_page_fm = ctk.Frame(main_fm, bg="black")
    Edit_page_lb = ctk.Label(Favorites_page_fm, text='Favorites', font=('Times New Roman', 13), fg='black')
    Edit_page_lb.pack(pady=80)
    Edit_page_fm.pack(fill=ctk.BOTH, expand=True)
    
    
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="")
    image = Image.open(file_path)   
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    
    
    
    
    
    

    
    
    canvas.pack()
    



















main_fm = ctk.Frame(root)
main_fm.pack(fill=ctk.BOTH, expand=True)

home_page()
app.mainloop()
root.mainloop()
