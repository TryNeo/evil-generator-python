# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox


URL = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'


class MainWindow:
    def __init__(self, root):
        root.title('Evil Generator | Python')
        root.geometry("500x400")

        #########centered screen##############
        root.update_idletasks()
        width = root.winfo_width()
        frm_width = root.winfo_rootx() - root.winfo_x()
        win_width = width + 2 * frm_width
        height = root.winfo_height()
        titlebar_height = root.winfo_rooty() - root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = root.winfo_screenwidth() // 2 - win_width // 2
        y = root.winfo_screenheight() // 2 - win_height // 2
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        root.deiconify()

        self.evil_screen(root)

    def evil_screen(self,root):
        self.result = tk.Text(root)
        self.result.pack()
        self.result.config(width=30, height=10, font=("Consolas",13), 
                    padx=15, pady=15)

        copy_text = tk.Button(root, text = 'Copiar texto',command=self.copy)
        copy_text.place(x=85, y=270)

        generate = tk.Button(root,text = 'Generar Insulto',command=self.evil_thread)
        generate.place(x=180,y=330)

        
    def evil_generator(self):
        try:
            self.response = requests.get(URL)
            if self.response.status_code == 200:
                self.insult = self.response.json()['insult']
                if len(self.insult) >= 0:
                    self.result.delete(1.0,"end")
                    self.result.insert(1.0, self.insult)
                else:
                    messagebox.showerror("Error", 'insulto no generado correctamente')
            else:
                messagebox.showerror("Error", 'Conexion no estable')
        except requests.exceptions.ConnectionError as error:
            messagebox.showerror("Error", 'Conexion no estable')

    def evil_thread(self):
        thread = threading.Thread(target=self.evil_generator)
        time.sleep(0.6)
        thread.start()


    def copy(self):
        messagebox.showerror("Error", 'Aun en proceso')

if __name__ == '__main__':
    main = tk.Tk()
    window = MainWindow(main)
    main.mainloop()