import tkinter as tk
from tkinter.colorchooser import askcolor

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("EasyBoard V1")

        self.pen_color = "black"
        self.pen_width = 3
        self.eraser_width = 10
        self.eraser_mode = False

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.bg_color = "white"
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.last_x = None
        self.last_y = None

        self.create_toolbar()

    def create_toolbar(self):
        """Create toolbar with pen, eraser, background, and size controls."""
        toolbar = tk.Frame(self.root)
        toolbar.pack(side="top", fill="x")

        color_button = tk.Button(toolbar, text="Pen Color", command=self.choose_color)
        color_button.pack(side="left")

        pen_size_label = tk.Label(toolbar, text="Pen Size")
        pen_size_label.pack(side="left")
        self.pen_size_slider = tk.Scale(toolbar, from_=1, to=10, orient="horizontal", command=self.update_pen_size)
        self.pen_size_slider.set(self.pen_width)
        self.pen_size_slider.pack(side="left")

        eraser_size_label = tk.Label(toolbar, text="Eraser Size")
        eraser_size_label.pack(side="left")
        self.eraser_size_slider = tk.Scale(toolbar, from_=1, to=30, orient="horizontal", command=self.update_eraser_size)
        self.eraser_size_slider.set(self.eraser_width)
        self.eraser_size_slider.pack(side="left")

        eraser_button = tk.Button(toolbar, text="Eraser", command=self.toggle_eraser)
        eraser_button.pack(side="left")

        pen_button = tk.Button(toolbar, text="Pen", command=self.toggle_pen)
        pen_button.pack(side="left")

        bg_color_button = tk.Button(toolbar, text="Background Color", command=self.change_background_color)
        bg_color_button.pack(side="left")

        clear_button = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_button.pack(side="left")

    def choose_color(self):
        """Open color picker for pen color."""
        color = askcolor()[1]
        if color:
            self.pen_color = color

    def update_pen_size(self, val):
        """Update the pen size."""
        self.pen_width = int(val)

    def update_eraser_size(self, val):
        """Update the eraser size."""
        self.eraser_width = int(val)

    def toggle_eraser(self):
        """Switch to eraser mode."""
        self.eraser_mode = True
        self.canvas.config(cursor="circle")

    def toggle_pen(self):
        """Switch back to pen mode."""
        self.eraser_mode = False
        self.canvas.config(cursor="crosshair")

    def paint(self, event):
        """Draw or erase on canvas."""
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            if self.eraser_mode:
                self.canvas.create_line(self.last_x, self.last_y, x, y, width=self.eraser_width, fill=self.bg_color, capstyle=tk.ROUND, smooth=True)
            else:
                self.canvas.create_line(self.last_x, self.last_y, x, y, width=self.pen_width, fill=self.pen_color, capstyle=tk.ROUND, smooth=True)

        self.last_x = x
        self.last_y = y

    def reset(self, event):
        """Reset last mouse position."""
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        """Clear all drawings without affecting background color."""
        self.canvas.delete("all")
        self.canvas.config(bg=self.bg_color)

    def change_background_color(self):
        """Change the background color."""
        color = askcolor()[1]
        if color:
            self.bg_color = color
            self.canvas.config(bg=self.bg_color)

if __name__ == "__main__":
    root = tk.Tk()
    whiteboard = Whiteboard(root)
    root.mainloop()
