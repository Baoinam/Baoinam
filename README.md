import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk
import os 
import tkinter.filedialog as tk_file


root = tk.Tk()
root.geometry("1000x600")
root.title("FotoFoto")
root.config(bg="white")

pen_color = "black"
pen_size = 5
file_path = ""



def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="D:/codefirst.io/Tkinter Image Editor/Pictures")
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=image, anchor="nw")
canvas = tk.Canvas(root, height=60, width=500)

image_list = []
image_vars = []

def display_images(index):
    image_display_lb.config(image=image_list[index][1])
    image_display_lb = tk.Label(root)
    image_display_lb.pack(anchor=tk.CENTER)
    
    file_path = tk_file.askdirectory()

    image_files = os.listdir(file_path)


    image_files = os.listdir(file_path)

    for r in range(0, len(image_files)):

        
        image_list.append([
            ImageTk.PhotoImage(Image.open(file_path + '/' + image_files[r]).resize((50, 50))), 
            ImageTk.PhotoImage(Image.open(file_path + '/' + image_files[r]).resize((480, 360)))]) 
        
        image_vars.append(f'img_{r}')
    
    slider = tk.Frame(canvas)
    canvas.create_window((10, 10), window=slider, anchor=tk.NW)
    for n in range(len(image_vars)):
        globals()[image_vars[n]] = tk.Button(slider, image=image_list[n][0], bd=0,
                                             command=lambda n=n:display_images(n))
    globals()[image_vars[n]].pack(side=tk.LEFT)

canvas.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar = ttk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar.config(command=canvas.xview)

canvas.config(xscrollcommand=x_scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

slider = tk.Frame(canvas)
canvas.create_window((10, 10), window=slider, anchor=tk.NW)


def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


def change_size(size):
    global pen_size
    pen_size = size


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')
    

def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas, anchor="nw")


def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


left_frame = tk.Frame(root, width=200, height=600, bg="white")
left_frame.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()

image_button = tk.Button(left_frame, text="Add Image",
                         command=add_image, bg="white")
image_button.pack(pady=15)

color_button = tk.Button(
    left_frame, text="Change Pen Color", command=change_color, bg="white")
color_button.pack(pady=5)

pen_size_frame = tk.Frame(left_frame, bg="white")
pen_size_frame.pack(pady=5)

pen_size_1 = tk.Radiobutton(
    pen_size_frame, text="Small", value=3, command=lambda: change_size(3), bg="white")
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(
    pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 = tk.Radiobutton(
    pen_size_frame, text="Large", value=7, command=lambda: change_size(7), bg="white")
pen_size_3.pack(side="left")

clear_button = tk.Button(left_frame, text="Clear",
                         command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
filter_label.pack()
filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur",
                                             "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()


filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))


canvas.bind("<B1-Motion>", draw)

root.mainloop()
