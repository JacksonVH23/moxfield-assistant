import tkinter as tk
from tkinter import *
from tkinter import ttk
from gui_theme import configure_theme

class appGUI:
    def __init__(self, master):
        self.master = master
        master.title("Moxfield Assistant")
        master.geometry("1200x800")
        
        master_background = '#28282B'
        master.configure(bg=master_background)
        configure_theme(master_background)

        # Make the window non-resizable
        master.resizable(False, False)

    def welcome_screen(self):
        # Create a label for "Welcome"
        welcome_label1 = ttk.Label(self.master, text="Welcome to the Moxfield Assistant!", style="welcome1.TLabel")
        welcome_label1.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        # Create a label for "Let's Get Building"
        welcome_label2 = ttk.Label(self.master, text="Let's Get Building", style="welcome2.TLabel")
        welcome_label2.place(relx=0.475, rely=0.5, anchor=tk.CENTER)
        # Create a button to the right of welcome_label2
        button_text = ">>>"
        button = ttk.Button(self.master, text=button_text, style='welcome.TButton', command=self.button_click)
        button.place(relx=0.6, rely=0.501, anchor=tk.CENTER)
    
    def button_click(self):
        # Define the action when the button is clicked
        print("Button clicked!")

    def selection_bar(self):
        bar = ttk.Notebook(self.master)
        
def run_gui():
    root = tk.Tk()
    gui = appGUI(root)
    gui.welcome_screen()
    gui.selection_bar()
    root.mainloop()
