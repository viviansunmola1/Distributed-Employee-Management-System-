import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import socket
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

    # ... (existing code)

    def submit_data_thread(self):
        try:
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

            # Display the JSON data in a message box
            json_data = json.loads(response)
            messagebox.showinfo("JSON Data", json.dumps(json_data, indent=4))

            s.close()

            # Update the GUI with the response from the server
            self.master.after(0, lambda: self.fn_entry.delete(0, tk.END))
            self.master.after(0, lambda: self.ln_entry.delete(0, tk.END))
            self.master.after(0, lambda: self.age_entry.delete(0, tk.END))
            self.master.after(0, lambda: self.emp_dropdown.set(""))
            self.master.after(0, lambda: messagebox.showinfo("Success", "Data submitted successfully!"))

        except ConnectionRefusedError:
            print("Error submitting data: connection refused")
            messagebox.showerror("Error", "Could not connect to server. Please try again later.")
        except Exception as e:
            print("Error submitting data:", e)
            messagebox.showerror("Error", "An error occurred while submitting data.")

if __name__ == '__main__':
    root = tk.Tk()
    form = EmployeeForm(master=root)
    form.mainloop()
