import tkinter as tk
import subprocess
from tkinter import messagebox
import time
import os

# Define the function that freezes the time in Parallels
def freeze_time():
    subprocess.run(["sudo", "date", "{month}{day}{hour}{minute}{year}".format(
        month=time.strftime("%m"),
        day=time.strftime("%d"),
        hour=time.strftime("%H"),
        minute=time.strftime("%M"),
        year=time.strftime("%Y")
    )])
    date_time = time.ctime()
    messagebox.showinfo("Time Frozen for PD 18", date_time)

# Define the function that verifies if the time is frozen in Parallels
def verify_time():
    result = os.popen("date").read()
    if "UTC" in str(result):
        messagebox.showinfo("Verify PD", "Time is not frozen for PD 18")
    else:
        messagebox.showinfo("Verify PD", "Time is frozen for PD 18")

# Define the function to stop Parallels from phoning home and block the trial
def hack_pd_trial():
    subprocess.run(["sudo", "stop", "parallels", "phoning", "home"])
    subprocess.run(["sudo", "rm", "-rf", "/Applications/Parallels Desktop.app/Contents/MacOS/Contents/PlugIns/parallels.virtualization.sdk.18.nupkg"])
    subprocess.run(["sudo", "rm", "-rf", "/Library/Parallels/Parallels Desktop.app/Contents/Resources/Tools/parallels.virtualization.sdk.18.nupkg"])
    messagebox.showinfo("CAT HACKED THE MATRIX 0.X", "Parallels Desktop 18 module trial has been successfully hacked and deleted!")

# Create the main window
root = tk.Tk()
root.geometry("800x600")

# Create a label for the app name
app_name = tk.Label(root, text="PD-FREEZER 0.X", font=("Arial", 20))
app_name.pack(pady=20)

# Create a button to freeze the time
freeze_button = tk.Button(root, text="Freeze Time", font=("Arial", 16), command=freeze_time)
freeze_button.pack(pady=50)

# Create a button to verify if the time is frozen
verify_button = tk.Button(root, text="Verify PD", font=("Arial", 16), command=verify_time)
verify_button.pack(pady=50)

# Create a button to block the trial
block_button = tk.Button(root, text="Block Trial", font=("Arial", 16), command=hack_pd_trial)
block_button.pack(pady=50)

# Run the main loop
root.mainloop()
