import tkinter as tk
from tkinter import ttk

def configure_theme(master_background):
    overall_style = ttk.Style()
    overall_style.theme_use('alt')
    label_style = ttk.Style()
    label_style.configure("welcome1.TLabel",
                          font=("Helvetica", 33, "bold"),
                          foreground="white",
                          background=master_background)
    label_style.configure("welcome2.TLabel",
                          font=("Helvetica", 23),
                          foreground="white",
                          background=master_background,
                          weight="bold")
    
    button_style = ttk.Style()
    button_style.configure('welcome.TButton',
                           background = "#4F7942",
                           foreground="white",
                           borderwidth=0,
                           font=("Helvetica", 14, "bold"),
                           padding=(-40, 0, -42, -1))
    button_style.map('welcome.TButton', background=[('active', '#355E3B')])
