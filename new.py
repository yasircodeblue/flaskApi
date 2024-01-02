import tkinter as tk
from tkinter import messagebox
import configparser

def save_credentials(username, password):
    config = configparser.ConfigParser()
    config['Credentials'] = {'Username': username, 'Password': password}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def authenticate(username, password):
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        saved_username = config.get('Credentials', 'Username')
        saved_password = config.get('Credentials', 'Password')

        if username == saved_username and password == saved_password:
            messagebox.showinfo('Authentication', 'Login successful!')
        else:
            messagebox.showerror('Authentication', 'Invalid credentials')
    except configparser.NoSectionError:
        messagebox.showerror('Authentication', 'No saved credentials found')

def login_clicked():
    # Try to read saved credentials
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        saved_username = config.get('Credentials', 'Username')
        saved_password = config.get('Credentials', 'Password')

        # Fill in the input fields with saved values
        username_entry.delete(0, tk.END)
        username_entry.insert(0, saved_username)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, saved_password)

    except (configparser.NoSectionError, configparser.NoOptionError):
        pass

def save_clicked():
    username = username_entry.get()
    password = password_entry.get()
    save_credentials(username, password)
    messagebox.showinfo('Save', 'Credentials saved successfully!')

# Create the main window
root = tk.Tk()
root.title('Login')

# Create and place widgets
username_label = tk.Label(root, text='Username:')
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text='Password:')
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text='Login', command=login_clicked)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

save_button = tk.Button(root, text='Save Credentials', command=save_clicked)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()