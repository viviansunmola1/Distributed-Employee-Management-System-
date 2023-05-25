# Vodafone-CDE (Vivian and Jabed) - Distributed Employee Management System
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import json
import threading

class EmployeeForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Employee Form")
        self.master.geometry("350x180")
        self.master.eval('tk::PlaceWindow . center')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="First Name").grid(row=0, pady=(5, 0))
        tk.Label(self, text="Last Name").grid(row=1)
        tk.Label(self, text="Age").grid(row=2)
        tk.Label(self, text="Employment Status").grid(row=3)

        vcmd_letter = (self.master.register(self.only_letters), '%S')
        vcmd_digit = (self.master.register(self.only_digits), '%S')

        self.fn_entry = tk.Entry(self, validate='key', validatecommand=vcmd_letter)
        self.ln_entry = tk.Entry(self, validate='key', validatecommand=vcmd_letter)
        self.age_entry = tk.Entry(self, validate='key', validatecommand=vcmd_digit)

        self.emp_status = tk.StringVar()
        emp_statuses = ["Employed", "Unemployed"]
        self.emp_dropdown = ttk.Combobox(self, textvariable=self.emp_status, values=emp_statuses, state='readonly')

        self.fn_entry.grid(row=0, column=1, pady=(5, 0))
        self.ln_entry.grid(row=1, column=1)
        self.age_entry.grid(row=2, column=1)
        self.emp_dropdown.grid(row=3, column=1)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=4, column=1, pady=(10, 0))

        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(5, weight=1)

    def only_letters(self, char):
        if char.isalpha() or char == '':
            return True
        else:
            return False

    def only_digits(self, char):
        if char.isdigit() or char == '':
            return True
        else:
            return False

    def submit_data(self):
        if not self.fn_entry.get() or not self.ln_entry.get() or not self.age_entry.get() or not self.emp_status.get():
            messagebox.showinfo("Error", "Please fill out all fields before submitting.")
        else:
            # Move the submission process to a separate thread to avoid the tkinter app from freezing
            threading.Thread(target=self.submit_data_thread).start()

    def submit_data_thread(self):
        try:
            employee = {
                'first_name': self.fn_entry.get(),
                'last_name': self.ln_entry.get(),
                'age': self.age_entry.get(),
                'employed': self.emp_status.get()
            }

            response = requests.post('http://localhost:5000/data', json=employee)
            print("Response from server:", response.text)

            # Update the GUI with the response from the server
            self.master.after(0, lambda: self.fn_entry.delete(0, tk.END))
            self.master.after(0, lambda: self.ln_entry.delete(0, tk.END))
            self.master.after(0, lambda: self.age_entry.delete(0, tk.END))
            self.master.after(0, lambda: self.emp_dropdown.set(""))
            self.master.after(0, lambda: messagebox.showinfo("Success", "Data submitted successfully!"))

        except requests.exceptions.ConnectionError:
            print("Error submitting data: connection refused")
            messagebox.showerror("Error", "Could not connect to server. Please try again later.")
        except Exception as e:
            print("Error submitting data:", e)
            messagebox.showerror("Error", "An error occurred while submitting data.")

if __name__ == '__main__':
    root = tk.Tk()
    form = EmployeeForm(master=root)
    form.mainloop()
