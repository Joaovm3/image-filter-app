from gui.main_window import MainWindow
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Image Filter Application")
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
