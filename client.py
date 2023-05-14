import tkinter as tk
from tkinter import ttk
import socket
import json

class EmployeeForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Employee Form")
        self.master.geometry("350x200")
        self.master.eval('tk::PlaceWindow . center')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="First Name").grid(row=0)
        tk.Label(self, text="Last Name").grid(row=1)
        tk.Label(self, text="Age").grid(row=2)
        tk.Label(self, text="Employment Status").grid(row=3)

        self.fn_entry = tk.Entry(self)
        self.ln_entry = tk.Entry(self)
        self.age_entry = tk.Entry(self)

        self.emp_status = tk.StringVar()
        emp_statuses = ["Employed", "Unemployed"]
        self.emp_dropdown = ttk.Combobox(self, textvariable=self.emp_status, values=emp_statuses)

        self.fn_entry.grid(row=0, column=1)
        self.ln_entry.grid(row=1, column=1)
        self.age_entry.grid(row=2, column=1)
        self.emp_dropdown.grid(row=3, column=1)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=4, column=1)

    def submit_data(self):
        host = 'localhost'
        port = 5000

        s = socket.socket()
        s.connect((host, port))

        employee = {}
        employee['first_name'] = self.fn_entry.get()
        employee['last_name'] = self.ln_entry.get()
        employee['age'] = self.age_entry.get()
        employee['employed'] = self.emp_status.get()

        data = json.dumps(employee)

        s.send(data.encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        print("Response from server:", response)

        s.close()

        self.fn_entry.delete(0, tk.END)
        self.ln_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.emp_dropdown.set("")

if __name__ == '__main__':
    root = tk.Tk()
    form = EmployeeForm(master=root)
    form.mainloop()
