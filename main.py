import tkinter as tk
import sqlite3
import datetime
import os
import qrcode
import shutil


#chanding working directory to where our main.py is, to use relative paths
abspath = os.path.abspath(__file__)
dir_name = os.path.dirname(abspath)
os.chdir(dir_name)
#

validate_msg = "Valider"
close_msg = "Fermer"
update_msg = "Mise à jour"
print_all_msg = "Télécharger"


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
        self.left_side_frame = tk.Frame(self)
        bottom_frame.pack(side="bottom")
        right_side_frame.pack(side="right")
        top_side_frame.pack(side="top")
        self.left_side_frame.pack(side="left", fill=tk.BOTH, expand=True)
        button1 = tk.Button(bottom_frame, width=8, height=2, text=validate_msg, command=self.validate_action)
        button2 = tk.Button(bottom_frame, width=8, height=2, text=close_msg, command=self.close_action)
        button3 = tk.Button(right_side_frame, width=10, height=2, text=update_msg, command=self.update_data)
        button4 = tk.Button(right_side_frame, width=10, height=2, text=print_all_msg, command=self.print_all)
        button1.grid(row=0, column=0, padx=10, pady=5)
        button2.grid(row=0, column=1, padx=10, pady=5)
        button3.grid(row=0, column=0, sticky=tk.N, padx=10, pady=5)
        button4.grid(row=1, column=0, sticky=tk.N, padx=10, pady=5)

    def validate_action(self):
        print("Enregistrer")

    def close_action(self):
        self.destroy()
        self.quit()

    def update_data(self):
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()
        conn = sqlite3.connect('bdd.db')
        c = conn.cursor()
        c.execute('SELECT * FROM data ORDER BY date')
        table_columns = [column[0] for column in c.description]
        self.data = eval(str(c.fetchall()))
        conn.close()
        for widget in self.left_side_frame.winfo_children():
            widget.destroy()
        self.data_grid = DataGrid(self.left_side_frame, table_columns, self.data)

    def print_all(self):
        self.make_qrcode()

    def make_qrcode(self):
        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10,
                           border=4)
        if not os.path.isdir("qrcode_img"):
            os.mkdir("qrcode_img")
        for i in range(len(self.data)):
            nserie = self.data[i][2]
            qr.add_data(nserie)
            qr.make(fit=True)
            img = qr.make_image()
            img.save("qrcode_img/" + nserie + ".jpg")

        shutil.make_archive("qrcode_img", 'zip', "qrcode_img")
        print("done")



class DataGrid(tk.Frame):
    def __init__(self, fenetre, table_columns=[], data=[]):
        tk.Frame.__init__(self, fenetre)
        self.fenetre = fenetre
        self.numberLines = len(data)
        self.numberColumns = len(data[0])
        self.pack(fill=tk.BOTH)
        self.data = list()

        for i in range(self.numberLines):
            line = list()
            for j in range(self.numberColumns):
                cell = tk.Label(self, text=str(data[i][j]))
                line.append(cell)
                cell.grid(row=i+1, column=j, padx=40)
            self.data.append(line)

        self.results = list()
        for i in range(self.numberColumns):
            cell = tk.Label(self, text=table_columns[i])
            cell.grid(row=0, column=i)
            self.results.append(cell)


if __name__ == "__main__":
    App()