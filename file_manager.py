from curses import window
from tkinter import *
import shutil
import os
from tkinter import filedialog
import easygui
from tkinter import messagebox as mb


# Opens file directory GUI, path is stored.
def open_window():
    open = easygui.fileopenbox()
    return open


# Open functionality
def open_file():

    # Calls GUI and stores path.
    window = open_window()

    try:
        # Opens file chosen.
        os.startfile(window)
    except:
        # If no file is present, gives error.
        mb.showinfo('confirmation', "File not found!")


# Copy/paste functionality
def copy_file():

    source = open_window()

    # Calls GUI and stores requested directory.
    destination = filedialog.askdirectory()

    # This copies the chose file, and pastes it in the directory requested.
    shutil.copy(source, destination)

    # Creates message box to alert success.
    mb.showinfo('confirmation', 'File Copied!')


# Delete functionality
def delete_file():
    del_file = open_window()

    # Checks file validity, deletes if valid.
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found!")


# Rename functionality
def rename_file():

    orig_file = open_window()

    # Saves directory path.
    path = os.path.dirname(orig_file)

    # Splits extension (.py) and root (file_manager) so the extension can be kept the same.
    extension = os.path.splitext(orig_file)[1]
    print("Enter a new name for the file: ")
    rename = input('')

    # Joins the previously split extension and root.
    path2 = os.path.join(path, rename+extension)
    print(path2)

    # Actual renaming function.
    os.rename(orig_file, path2)
    mb.showinfo('confirmation', "File has been renamed...")
