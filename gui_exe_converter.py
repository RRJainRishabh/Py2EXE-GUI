import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_script():
    filepath = filedialog.askopenfilename(
        title="Select Python Script",
        filetypes=[("Python files", "*.py")])
    if filepath:
        script_path.set(filepath)

def convert_to_exe():
    script = script_path.get()
    if not script or not os.path.isfile(script):
        messagebox.showerror("Error", "Please select a valid Python script.")
        return

    try:
        subprocess.run(["pyinstaller", "--onefile", script], check=True)
        messagebox.showinfo("Success", "Executable created successfully in 'dist' folder.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to create executable.")

# GUI setup
root = tk.Tk()
root.title("Python to EXE Converter")
root.geometry("500x150")

script_path = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(frame, textvariable=script_path, width=50)
entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

browse_btn = tk.Button(frame, text="Browse", command=browse_script)
browse_btn.grid(row=0, column=1, padx=5, pady=5)

convert_btn = tk.Button(frame, text="Convert to EXE", command=convert_to_exe)
convert_btn.grid(row=1, column=0, columnspan=2, pady=10)

frame.columnconfigure(0, weight=1)
root.mainloop()
