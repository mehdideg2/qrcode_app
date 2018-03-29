import tkinter as tk
import sqlite3
from sqlite3 import Error
import datetime

validate_msg = "Valider"
close_msg = "Fermer"
update_msg = "Mise à jour"


class App(tk.Tk):
    MAIN_WINDOW_SIZE = 800, 500

    def __init__(self):
        tk.Tk.__init__(self, None)
        self.center_window(self.MAIN_WINDOW_SIZE)
        self.gui_structure()
        self.mainloop()

    def center_window(self, size):
        self.update_idletasks()
        x = self.winfo_screenwidth() / 2 - size[0] / 2
        y = self.winfo_screenheight() / 2 - size[1] / 2
        self.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def gui_structure(self):
        bottom_frame = tk.Frame(self)
        top_side_frame = tk.Frame(self)
        right_side_frame = tk.Frame(self)
        left_side_frame = tk.Frame(self)
        bottom_frame.pack(side="bottom")
        right_side_frame.pack(side="right")
        top_side_frame.pack(side="top")
        left_side_frame.pack(side="left")
        button1 = tk.Button(bottom_frame, width=8, height=2, text=validate_msg, command=self.validate_action)
        button2 = tk.Button(bottom_frame, width=8, height=2, text=close_msg, command=self.close_action)
        button3 = tk.Button(right_side_frame, width=8, height=2, text=update_msg, command=self.update_data)
        button1.grid(row=0, column=0, padx=10, pady=5)
        button2.grid(row=0, column=1, padx=10, pady=5)
        button3.grid(row=0, column=0, sticky=tk.N, padx=10, pady=5)

    def validate_action(self):
        print("Enregistrer")

    def close_action(self):
        self.destroy()
        self.quit()

    def update_data(self):
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        nserie = 123

        conn = sqlite3.connect('bdd.db')
        c = conn.cursor()
        c.execute('SELECT * FROM data')
        print(c.fetchone())


if __name__ == "__main__":
    App()