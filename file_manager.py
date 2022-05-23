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
