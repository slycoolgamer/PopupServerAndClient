import socket
import tkinter as tk
from tkinter import messagebox


class PopupGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.popup_label = tk.Label(self, text="Enter Popup Message:")
        self.popup_label.pack(side="top")

        self.popup_entry = tk.Entry(self)
        self.popup_entry.pack(side="top")

        self.popup_button = tk.Button(self)
        self.popup_button["text"] = "Generate Popup"
        self.popup_button["command"] = self.generate_popup
        self.popup_button.pack(side="bottom")

    def generate_popup(self):
        
        popup_text = self.popup_entry.get()

        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 65432))
            s.sendall(popup_text.encode())

        
        messagebox.showinfo("Popup", popup_text)


root = tk.Tk()
app = PopupGenerator(master=root)
app.mainloop()
