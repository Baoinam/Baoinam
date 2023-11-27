import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import os 

class PhotoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FotoFoto Editor App")

       
        self.image_path = ""
        self.original_image = None
        self.current_image = None
        self.canvas = None
        self.draw = None
        self.pen_color = "black"
        self.pen_size = 1

        # Create GUI
        self.create_menu()
        self.create_canvas()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Return To FotoFoto Viewer", command=return_to)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Clear Filters", command=self.clear_filters)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        color_menu = tk.Menu(menu_bar, tearoff=0)
        color_menu.add_command(label="Choose Pen Color", command=self.choose_pen_color)
        color_menu.add_command(label="Reset Pen Color", command=self.reset_pen_color)
        menu_bar.add_cascade(label="Pen Color", menu=color_menu)

        pen_menu = tk.Menu(menu_bar, tearoff=0)
        pen_menu.add_command(label="Increase Pen Size", command=self.increase_pen_size)
        pen_menu.add_command(label="Decrease Pen Size", command=self.decrease_pen_size)
        pen_menu.add_command(label="Clear Drawing", command=self.clear_drawing)
        menu_bar.add_cascade(label="Pen Options", menu=pen_menu)

        filter_menu = tk.Menu(menu_bar, tearoff=0)
        filter_menu.add_command(label="Black and White", command=lambda: self.apply_filter("black_and_white"))
        filter_menu.add_command(label="Blur", command=lambda: self.apply_filter("blur"))
        filter_menu.add_command(label="Sharpen", command=lambda: self.apply_filter("sharpen"))
        filter_menu.add_command(label="Smooth", command=lambda: self.apply_filter("smooth"))
        filter_menu.add_command(label="Emboss", command=lambda: self.apply_filter("emboss"))
        menu_bar.add_cascade(label="Filter", menu=filter_menu)

        self.root.config(menu=menu_bar)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.canvas.bind("<B1-Motion>", self.paint)
    

    def open_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.reset_image()
            self.display_image()
    

    def reset_image(self):
        self.current_image = self.original_image.copy()
        self.draw = None
    

    def display_image(self):
        self.image_tk = ImageTk.PhotoImage(self.current_image)
        self.canvas.config(width=self.current_image.width, height=self.current_image.height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

    def save_image(self):
        if self.current_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                       filetypes=[("PNG files", "*.png")])
            if save_path:
                self.current_image.save(save_path)

    def apply_filter(self, filter_type):
        if self.current_image:
            if filter_type == "black_and_white":
                self.current_image = self.current_image.convert("L")
            elif filter_type == "blur":
                self.current_image = self.current_image.filter(ImageFilter.BLUR)
            elif filter_type == "sharpen":
                self.current_image = self.current_image.filter(ImageFilter.SHARPEN)
            elif filter_type == "smooth":
                self.current_image = self.current_image.filter(ImageFilter.SMOOTH)
            elif filter_type == "emboss":
                self.current_image = self.current_image.filter(ImageFilter.EMBOSS)
            self.display_image()

    def clear_filters(self):
        self.reset_image()
        self.display_image()

    def choose_pen_color(self):
        color = colorchooser.askcolor(initialcolor=self.pen_color)[1]
        if color:
            self.pen_color = color

    def reset_pen_color(self):
        self.pen_color = "black"

    def increase_pen_size(self):
        self.pen_size += 5

    def decrease_pen_size(self):
        if self.pen_size > 1:
            self.pen_size -= 1

    def clear_drawing(self):
        self.reset_image()
        self.display_image()

    def paint(self, event):
        if self.current_image:
            if not self.draw:
                self.draw = ImageDraw.Draw(self.current_image)
            x1, y1 = (event.x - self.pen_size), (event.y - self.pen_size)
            x2, y2 = (event.x + self.pen_size), (event.y + self.pen_size)
            self.draw.line([x1, y1, x2, y2], fill=self.pen_color, width=self.pen_size * 2)
            self.display_image()

filename = "ImageViewer.py"
def return_to():
    root.destroy()
    os.system(f"python {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoEditorApp(root)
    root.mainloop()
