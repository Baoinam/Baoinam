import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tk_file
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry('500x500')
root.title('FotoFoto')


def popup_menu(e):
    menu_bar.tk_popup(x=e.x_root, y=e.y_root)


image_list = []
image_vars = []


def display_images(index):
    image_display_lb.config(image=image_list[index][1])


def load_images():
    dir_path = tk_file.askdirectory()

    image_files = os.listdir(dir_path)

    for r in range(0, len(image_files)):
        image_list.append([
            ImageTk.PhotoImage(Image.open(dir_path + '/' + image_files[r]).resize((50, 50))),
            ImageTk.PhotoImage(Image.open(dir_path + '/' + image_files[r]).resize((480, 360)))])

        image_vars.append(f'img_{r}')

    for n in range(len(image_vars)):
        globals()[image_vars[n]] = tk.Button(slider, image=image_list[n][0], bd=0,
                                             command=lambda n=n: display_images(n))
        globals()[image_vars[n]].pack(side=tk.LEFT)


def open_editor_page():
    root.destroy()
    os.system("EditingPage.py")


# Buttons

editor_page_btn = tk.Button(root, text='Edit', bd=0, font=('Bold', 15),
                            command=open_editor_page)
editor_page_btn.pack(side=tk.TOP, anchor=tk.W, pady=20, padx=20)

menu_btn = tk.Button(root, text='Open Folder', bd=0, font=('Bold', 15))
menu_btn.pack(side=tk.TOP, anchor=tk.W, pady=10, padx=20)
menu_btn.bind('<Button-1>', popup_menu)

menu_bar = tk.Menu(root, tearoff=False)
menu_bar.add_command(label='Open Folder', command=load_images)

image_display_lb = tk.Label(root)
image_display_lb.pack(anchor=tk.CENTER)

canvas = tk.Canvas(root, height=60, width=500)
canvas.pack(side=tk.BOTTOM, fill=tk.X)
# scroll bar button
x_scroll_bar = ttk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar.config(command=canvas.xview)

canvas.config(xscrollcommand=x_scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

slider = tk.Frame(canvas)
canvas.create_window((10, 10), window=slider, anchor=tk.NW)

root.mainloop()
